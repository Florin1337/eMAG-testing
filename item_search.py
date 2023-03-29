from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import openpyxl

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.emag.ro/")

search = driver.find_element("id", "searchboxTrigger")
search.send_keys("mouse logitech")
search.submit()

wait = WebDriverWait(driver, 10)

produs_list = driver.find_elements("xpath", "//*[@id=\"card_grid\"]/div")

workbook = openpyxl.Workbook()
sheet = workbook.active

for produs in produs_list:
    name = produs.find_elements("css selector", "a[data-zone='title']")
    price = produs.find_elements("css selector", "p.product-new-price")
    if name and price:
        sheet.append([name[0].text, price[0].text])

workbook.save("emag.xlsx")
