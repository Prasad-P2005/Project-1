from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pyautogui
import keyboard
import time


def get_text_to_type(driver):
    """Extracts text to type from the Typeracer page."""
    time.sleep(2)  # Give time for the page to load
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    span = soup.findAll("span")
    text = ""

    for i in span:
        if "unselectable" in str(i):
            text += i.text

    if not text:
        print("No text found!")
        return None
    else:
        print("Text to type:", text)
    return text


def type_text(text):
    """Simulates typing the extracted text."""
    pyautogui.typewrite(text, interval=0.06)


def main():
    """Main function to start the browser, extract text, and type it."""
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium-browser"
    chrome_options.add_experimental_option("detach", True)

    # Required arguments for running Chrome smoothly
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://play.typeracer.com")

    print(" Press CTRL + ALT + T to start typing...")

    keyboard.wait("ctrl+alt+t")  # Wait for user to trigger typing
    text_to_type = get_text_to_type(driver)

    if text_to_type:
        type_text(text_to_type)  # Simulate typing


if __name__ == "__main__":
    main()
