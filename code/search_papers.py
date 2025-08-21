# References:
# https://www.youtube.com/watch?v=APpm80uxv1g

## import libraries
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

## declare global vars here

chrome_options = Options()
# Options below are useful for running on server or deploying to docker container
#chrome_options.add_arguments("--no-sandbox")
#chrome_options.add_arguments("--headless")
#chrome_options.add_arguments("--disable-dec-shm-usage")
#chrome_options.add_arguments("--verbose")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = "https://dl.acm.org/"

## initialize LLM here

## ACM DL uses cookies, need to bypass to automate
def bypass_cookies():
    driver.get(url)
    try:
        # try loading pickle cookies file if exists
        with open("cookies.pkl", "rb") as f:
            print("Using existing cookie info.")
            cookies = pickle.load(f) # loads cookies from file
            for cookie in cookies:
                driver.add_cookie(cookie) # sets cookies already created
            driver.get(url) # now nav to url
    except FileNotFoundError: # will be the case the first time this runs
        print("No cookies found. Clicking 'Use necessary cookies only'...")
        try:
            # wait for iframe to appear
            iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='Cookiebot']"))
            )
            driver.switch_to.frame(iframe)

            # wait for the button inside iframe
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyButtonDecline"))
            )
            cookie_button.click()
            print("Cookie button clicked.")
            time.sleep(2)
            driver.switch_to.default_content()  # back to main page
        except Exception as e:
            print("Could not click cookie button:", e)
    
    with open('cookies.pkl', 'wb') as f:
        pickle.dump(driver.get_cookies(), f) # dumps all cookies into filestream
    
    driver.get(url) # just here to see results, can prob remove later
    time.sleep(5)
    print("Done.")

## For each result in query results, get title and abstract

    ## Have LLM look through title and abstract, determine if paper should be included

    ## If paper is included, store in JSON file (prob want to strategize this part later)