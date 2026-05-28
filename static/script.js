const button = document.getElementById("runBtn");
const input = document.getElementById("textToAnalyze");
const result = document.getElementById("result");

button.addEventListener("click", async () => {
  const text = input.value.trim();

  if (!text) {
    result.textContent = "Invalid text! Please try again.";
    return;
  }

  try {
    const response = await fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`);
    result.textContent = await response.text();
  } catch (error) {
    result.textContent = "Invalid text! Please try again.";
  }
});

