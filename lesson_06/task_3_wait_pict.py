from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
pict = driver.find_element(By.CSS_SELECTOR, '#award')
src = pict.get_attribute('src')
print(f'значение src:{src}')
driver.quit()
