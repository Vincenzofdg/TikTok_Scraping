from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException
from service.selenium_functions import xpath, class_name
import elements.tiktok as elem


# FireFox settings
# setting = Options()
# setting.add_argument("--disable-extensions")
# setting.add_argument("--disable-gpu")
# setting.add_argument("--no-sandbox")
# setting.add_argument("--disable-dev-shm-usage")
# setting.add_argument("--headless")

# web = webdriver.Firefox(options=setting)
web = webdriver.Firefox()

web.get(elem.url)

close = xpath(elem.close, web)
close.click()


# Localiza o elemento Shadow DOM
shadow_root = web.execute_script('return document.querySelector("#shadow-root-id")')
input_field = shadow_root.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/form/input//div[2]/div[2]/div')

# Preenche o campo de texto dentro do Shadow DOM
response = web.request('POST', '/session/$sessionId/shadow/dom', json={
    'script': 'arguments[0].value = arguments[1]',
    'args': [input_field, 'Texto a ser preenchido']
})




input = xpath(elem.input, web)
input.send_keys('skyrim')

# input.send_keys(Keys.RETURN)