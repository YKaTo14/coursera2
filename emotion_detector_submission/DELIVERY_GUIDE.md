# Emotion Detector Delivery Guide

## 1) Push this folder to a new GitHub repo

Use PowerShell from:

`C:\Users\javpu\OneDrive\Documents\coursera`

```powershell
cd C:\Users\javpu\OneDrive\Documents\coursera
git status
git checkout -b codex/emotion-detector-submission
git add emotion_detector_submission
git commit -m "Add emotion detector submission files"
```

Create a new empty GitHub repo on GitHub, then set the new remote:

```powershell
git remote set-url origin https://github.com/<your-username>/<your-new-repo>.git
git push -u origin codex/emotion-detector-submission
```

If you want the repo root to contain only the emotion detector project, create a separate repo and push this folder as-is from a fresh clone, or copy the contents of `emotion_detector_submission` into the repo root before committing.

## 2) Q1-Q16 paste-ready answer sheet

Replace the URL placeholders with your actual public GitHub links.

### Q1

`https://github.com/<your-username>/<your-new-repo>/blob/main/README.md`

### Q2

Paste the code from:

`C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission\EmotionDetection\emotion_detection.py`

### Q3

Paste your terminal output for application import/test.

### Q4

Paste the formatted code from:

`C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission\EmotionDetection\emotion_detection.py`

### Q5

Paste your formatted-output terminal output.

### Q6

`https://github.com/<your-username>/<your-new-repo>/blob/main/EmotionDetection/__init__.py`

### Q7

Paste your packaging test terminal output.

### Q8

Paste the code from:

`C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission\test_emotion_detection.py`

### Q9

Paste your unit test terminal output.

### Q10

Paste the code from:

`C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission\server.py`

### Q11

Upload:

`C:\Users\javpu\OneDrive\Pictures\Screenshots\6b_deployment_test.png`

### Q12

Paste the error-handling version from:

`C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission\EmotionDetection\emotion_detection.py`

### Q13

Paste the error-handling server code from:

`C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission\server.py`

### Q14

Upload:

`C:\Users\javpu\OneDrive\Pictures\Screenshots\7c_error_handling_interface.png`

### Q15

Paste the static-analysis version from:

`C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission\server.py`

### Q16

Paste your pylint score output.

## 3) Screenshot flow

### Deployment screenshot

1. Open a terminal in `C:\Users\javpu\OneDrive\Documents\coursera\emotion_detector_submission`
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the server:

```powershell
python server.py
```

4. Open the browser to:

`http://127.0.0.1:5000`

5. Type a sample text like:

`I am very happy today`

6. Click `Analyze`
7. Take screenshot as:

`C:\Users\javpu\OneDrive\Pictures\Screenshots\6b_deployment_test.png`

### Error-handling screenshot

1. Keep the server running
2. Open:

`http://127.0.0.1:5000`

3. Leave the input blank
4. Click `Analyze`
5. Confirm it shows:

`Invalid text! Please try again.`

6. Take screenshot as:

`C:\Users\javpu\OneDrive\Pictures\Screenshots\7c_error_handling_interface.png`

## 4) Pylint flow

Run your static analysis in the submission folder and paste the score output into Q16.

Example:

```powershell
pylint server.py
```

If `pylint` is not installed in your environment, install it first in the same Python environment you use for the project.

