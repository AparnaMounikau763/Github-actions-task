import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_exe_web_app():
    # Start EXE
    process = subprocess.Popen(["dist/main.exe"])

    time.sleep(5)  # wait for server

    options = Options()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:5000")

    assert "Hello, This is a Test Application!" in driver.page_source

    driver.quit()
    process.terminate()