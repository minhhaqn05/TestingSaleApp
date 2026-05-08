from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(execute_path='../../.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://vnexpress.net/')

articles = driver.find_elements(By.CSS_SELECTOR, '#automation_TV0 > article')
for article in articles:
    title = article.find_element(By.TAG_NAME, 'h3')
    des = article.find_element(By.CLASS_NAME, 'description')
    img = article.find_element(By.CSS_SELECTOR, '.thumb-art img, .thumb-art videos')
    print(title.text)
    print(des.text)
    print(img.get_attribute('src'))
    print('--------------------')

driver.quit()