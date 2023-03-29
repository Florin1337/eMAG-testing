from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

class teste:
    def login_valid():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("xosip70068@galcake.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("Real Name")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("P@rol4")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("P@rol4")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

        multifactor = driver.find_element("xpath", "//*[@id=\"main-container\"]/div[2]/div[2]/a[2]")
        multifactor.click()

    def email_empty():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys(" ")
        email.submit()
        time.sleep(10)

    def email_short():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("b@mailfals.com")
        email.submit()
        time.sleep(10)

    def email_long():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("verylongemailthatcouldnotbepossibleandwhatdoidoeventypingthislongemailbruhithinkthemaximurcharacterlenghtforemailonemagis96charactersbutwewillseesoonenough@gmail.com")
        email.submit()
        time.sleep(10)

    def email_invalidformat():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("abc123")
        email.submit()
        time.sleep(10)

    def email_registered():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("bocseflorin@yahoo.com")
        email.submit()
        time.sleep(10)

    def registration_name():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("teretam844@oniecan.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("P@rol4")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("P@rol4")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

    def arabic_name():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("teretam844@oniecan.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("مُحَمَّد")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("P@rol4")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("P@rol4")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

    def short_name():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("teretam844@oniecan.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("a")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("P@rol4")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("P@rol4")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

    def long_name():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("teretam844@oniecan.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("averylongusernamefdsdsgfdsahgfdshdfgshfgsfhgdfghhgfdgfhgfhdhgfhgfdghfddffdfddffddffdfdgdfgfsdjhtgfshgfsghfshfgdsgfshhfdshdgfhfgdshfgdshgfhsg")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("P@rol4")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("P@rol4")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

    def number_name():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("teretam844@oniecan.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("firstname1337")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("P@rol4")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("P@rol4")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

    def specialch_name():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("teretam844@oniecan.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("firstname fl@rin")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("P@rol4")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("P@rol4")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

    def empty_password():
        driver.get("https://auth.emag.ro/user/login")

        email = driver.find_element("id", "user_login_email")
        email.send_keys("teretam844@oniecan.com")
        email.submit()
        time.sleep(10)

        name = driver.find_element("id", "user_register_full_name")
        name.send_keys("firstname lastname")

        password1 = driver.find_element("id", "user_register_password_first")
        password1.send_keys("")

        password2 = driver.find_element("id", "user_register_password_second")
        password2.send_keys("")

        terms = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label")
        terms.click()

        register = driver.find_element("id", "user_register_continue")
        register.click()

    def run_tests():
        teste.login_valid()
        teste.email_empty()
        teste.email_short()
        teste.email_long()
        teste.email_invalidformat()
        teste.email_registered()
        teste.registration_name()
        teste.arabic_name()
        teste.short_name()
        teste.long_name()
        taste.number_name()
        taste.specialch_name()
        taste.empty_password()

teste.run_tests()