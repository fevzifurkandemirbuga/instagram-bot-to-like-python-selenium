from selenium import webdriver
from selenium.webdriver.common.by import By
import time

while True:
    USERNAME = input("Kullanıcı adı: ")
    PASSWORD = input("Şifre: ")
    NameOfPageToLike = input("Beğenilecek sayfanın adı: ")
    if USERNAME == "" or PASSWORD == "" or NameOfPageToLike == "":
        print("Lütfen kullanıcı adı, şifre ve beğenilecek sayfanın adını giriniz.")
    else:
        break

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(3)
# ****************************** GİRİŞ **************************************************
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
login = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
login.click()
time.sleep(10)
# ******************************** şimdi değil ************************************************
driver.find_element(By.CSS_SELECTOR, "._acao").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "._a9-z button").click()
time.sleep(2)
# ****************************** sayfaya giriş ******************************
driver.find_elements(By.CLASS_NAME,"x1i10hfl")[2].click()
searchBar=driver.find_element(By.CLASS_NAME,"_aauy")
# searchBar.click()
searchBar.send_keys(NameOfPageToLike)
time.sleep(2)
driver.find_elements(By.CLASS_NAME,"x1i10hfl")[10].click()
time.sleep(5)
# ****************************** post sayısı ********************************
post_number = int(driver.find_element(By.CSS_SELECTOR, "._ac2a").text)

driver.find_element(By.CSS_SELECTOR, "._aabd a").click()  # ilk post
time.sleep(3)
for i in range(post_number-1):
    value_of_button = driver.find_element(By.CSS_SELECTOR, "._aamu button svg").get_attribute("aria-label")
    if value_of_button == "Beğen":
        driver.find_element(By.CSS_SELECTOR, "._aamu button").click()
    driver.find_element(By.CSS_SELECTOR, "._aaqg button").click()
    time.sleep(2)
value_of_button = driver.find_element(By.CSS_SELECTOR, "._aamu button svg").get_attribute("aria-label")
if value_of_button == "Beğen":
    driver.find_element(By.CSS_SELECTOR, "._aamu button").click()
time.sleep(5)
driver.close()