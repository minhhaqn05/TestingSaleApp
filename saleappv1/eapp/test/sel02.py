from pygments.styles.dracula import comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(execute_path='../../.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://tiki.vn/dien-thoai-may-tinh-bang/c1789')

driver.execute_script('window.scrollTo(0, 300)')
driver.implicitly_wait(1)

products = driver.find_elements(By.CLASS_NAME, 'product-item')
pages = []
for p in products[:3]:
    print(p.get_attribute('href'))
    name = p.find_element(By.TAG_NAME, 'h3')
    pages.append(p.get_attribute('href'))
    print(name.text)

print('----- comments -----')
for idx, p in enumerate(pages):
    print('---', p)
    driver.get(p)
    driver.save_screenshot((f'product{idx}.png'))


    driver.execute_script('window.scrollTo(0, 2000)')
    driver.execute_script('window.scrollTo(0, 2000)')
    driver.execute_script('window.scrollTo(0, 2000)')
    driver.implicitly_wait(1)
    comments = driver.find_elements(By.CLASS_NAME, 'review-comment__content')
    for c in comments:
        print(c.text)

driver.quit()