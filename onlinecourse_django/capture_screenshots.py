"""Capture the assignment screenshots for the OnlineCourse demo project."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path
from urllib.request import urlopen

import django
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinecourse_project.settings")
django.setup()

from onlinecourse.models import Choice, Course, Question  # noqa: E402


CHROME_BINARY = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROMEDRIVER = BASE_DIR / ".drivers" / "chromedriver-win64" / "chromedriver.exe"
ADMIN_URL = "http://127.0.0.1:8000/admin/login/?next=/admin/"
SITE_URL = "http://127.0.0.1:8000/"


def build_driver():
    options = Options()
    options.binary_location = CHROME_BINARY
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1600,1800")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument(f"--user-data-dir={BASE_DIR / '.chrome-profile'}")
    return webdriver.Chrome(service=Service(str(CHROMEDRIVER)), options=options)


def wait_for_site(url: str, timeout_seconds: int = 30):
    deadline = time.time() + timeout_seconds
    last_error = None
    while time.time() < deadline:
        try:
            with urlopen(url) as response:  # noqa: S310
                if response.status == 200:
                    return
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(1)
    raise RuntimeError(f"Site did not become ready in time: {last_error}")


def capture_admin(driver):
    driver.get(ADMIN_URL)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.ID, "id_username")))
    driver.find_element(By.ID, "id_username").send_keys("admin")
    driver.find_element(By.ID, "id_password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content-main")))
    driver.set_window_size(1600, 1800)
    driver.save_screenshot(str(BASE_DIR / "03-admin-site.png"))


def capture_result(driver):
    course = Course.objects.get(slug="mock-exam")
    questions = list(Question.objects.filter(lesson__course=course).order_by("lesson__order", "order"))
    correct_choices = {
        question.id: Choice.objects.filter(question=question, is_correct=True).values_list("id", flat=True).first()
        for question in questions
    }

    driver.get(SITE_URL)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.ID, "student_name")))
    driver.find_element(By.ID, "student_name").send_keys("Codex Student")

    for question in questions:
        choice_id = correct_choices[question.id]
        selector = f'input[name="question_{question.id}"][value="{choice_id}"]'
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        driver.find_element(By.CSS_SELECTOR, selector).click()

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Congratulations')]")))
    driver.set_window_size(1600, 1600)
    driver.save_screenshot(str(BASE_DIR / "07-final.png"))


def main():
    server = subprocess.Popen(
        [
            sys.executable,
            "manage.py",
            "runserver",
            "127.0.0.1:8000",
        ],
        cwd=str(BASE_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        wait_for_site(SITE_URL)
        driver = build_driver()
        try:
            capture_admin(driver)
            capture_result(driver)
        finally:
            driver.quit()
    finally:
        server.terminate()
        try:
            server.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == "__main__":
    main()
