from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os

def scrape_reviews(url):
    driver = webdriver.Chrome(service=Service("chromedriver.exe"))
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-details-container"))
        )
    except:
        print("Product details did not load.")
        driver.quit()
        return None

    try:
        container = driver.find_element(By.CLASS_NAME, "product-details-container")
        brand = container.find_element(By.CLASS_NAME, "product-details-brand").text.strip()
        product_name = container.find_element(By.CLASS_NAME, "product-details-name").text.strip()
    except:
        brand, product_name = "N/A", "N/A"

    product_id = url.split("/")[-1]

    same_count_tries = 0
    previous_count = -1
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 800);")
        time.sleep(1.5)

        reviews = driver.find_elements(By.CLASS_NAME, "user-review-userReviewWrapper")
        current_count = len(reviews)
        if current_count == previous_count:
            same_count_tries += 1
            if same_count_tries >= 3:
                break
        else:
            same_count_tries = 0
            previous_count = current_count
        time.sleep(1)

    reviews_data = []
    for r in reviews:
        try:
            rating = r.find_element(By.CLASS_NAME, "user-review-starRating").text.strip()
        except:
            rating = "N/A"
        try:
            review_text = r.find_element(By.CLASS_NAME, "user-review-reviewTextWrapper").text.strip()
        except:
            review_text = "N/A"
        try:
            meta = r.find_element(By.CLASS_NAME, "user-review-left")
            spans = meta.find_elements(By.TAG_NAME, "span")
            date = spans[1].text.strip() if len(spans) > 1 else "N/A"
        except:
            date = "N/A"

        reviews_data.append({"date": date, "rating": rating, "review": review_text})

    driver.quit()

    output = {
        "product_id": product_id,
        "brand": brand,
        "product_name": product_name,
        "reviews": reviews_data
    }

    with open("myntra_reviews.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("Reviews saved to myntra_reviews.json")

# scrape_reviews("https://www.myntra.com/reviews/30396659")
