from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.emag.ro/")

def add_items_to_cart(*items):
    for item in items:
        search = driver.find_element("id", "searchboxTrigger")
        search.clear()
        search.send_keys(item)
        search.submit()
        time.sleep(1)

        select = driver.find_element("xpath", "//*[@id=\"card_grid\"]/div[1]/div/div/div[4]/div[2]/form/button")
        select.click()
        time.sleep(1)

    driver.get("https://www.emag.ro/cart/products?ref=cart")
    time.sleep(2)
    command = driver.find_element("xpath", "//*[@id=\"cart-products\"]/div/div[2]/div[1]/div/div[2]/div/a")
    command.click()


add_items_to_cart("mouse logitech", "mouse razer", "tastatura redragon")
