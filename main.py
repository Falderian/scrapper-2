from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import waitCheckHtmlExisting
from json import loads
from os import getcwd
import csv

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

browser = webdriver.Chrome(options=options)
browser.get(
    "http://localhost:5500/Smoke_%20Accessories%20%E2%80%93%20Austin%20Wholesale%20Supply.html"
)

target = (By.CSS_SELECTOR, "div[class*=' col-6 col-sm-6 col-md-4 col-lg-3 col-xl-3']")
waitCheckHtmlExisting(browser, By.TAG_NAME, "form")

cards = browser.find_elements(*target)

with open(getcwd() + "/data.csv", "w") as data_file:
    columns_names = [
        "@context",
        "@type",
        "name",
        "url",
        "image",
        "description",
        "sku",
        "brand-type",
        "brand-name",
        "offers-type",
        "offers-sku",
        "offers-availability",
        "offers-price",
        "offers-priceCurrency",
        "offers-url",
    ]

    write = csv.writer(data_file)
    write.writerow(columns_names)

    for card in cards:
        json_format = loads(
            card.find_element(By.TAG_NAME, "script").get_attribute("innerText")
        )
        converted = [
            json_format["@context"],
            json_format["@type"],
            json_format["name"],
            json_format["url"],
            json_format["image"][0] if "image" in json_format else "None",
            json_format["description"],
            json_format["sku"],
            json_format["brand"].values(),
            json_format["offers"][0].values(),
        ]
        write.writerow(converted)
