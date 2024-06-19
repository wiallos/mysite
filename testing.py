from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C://drivers//chromewdriver.exe"

driver = webdriver.Chrome()  

try:

    driver.get("http://127.0.0.1:5000/")
   
    time.sleep(3)

    title = driver.title
    

    if "Neirow" in title:
        print("Тест пройден: 'Neirow' найдено в заголовке")
    else:
        print("Тест провален: 'Neirow' не найдено в заголовке")

finally:

    driver.quit()


def get_meta_content(driver, name):
    meta_tag = driver.find_element(By.XPATH, f'//meta[@name="{name}"]')
    
    return meta_tag.get_attribute('content')

driver = webdriver.Chrome()  

try:
   
    driver.get("http://127.0.0.1:5000/") 
    
    time.sleep(3)
 
    keywords_content = get_meta_content(driver, 'keywords')

   
    required_keywords = ["Rina Pusheen", "фотограф Rina Pusheen", "портфолио Neirow"]
  
    for keyword in required_keywords:
        if keyword in keywords_content:
            print(f"Тест пройден: '{keyword}' найден в ключевых словах мета-тега")
        else:
            print(f"Тест провален: '{keyword}' не найдены в ключевых словах мета-тега")

finally:
   
    driver.quit()



driver = webdriver.Chrome()  

try:
    
    driver.get("http://127.0.0.1:5000/")
    
 
    time.sleep(3)

    links = driver.find_elements(By.TAG_NAME, "a")
    
  
    for link in links:
        try:
           
            ActionChains(driver).move_to_element(link).perform()
            time.sleep(2)
            
           
            link_text = link.text
            link.click()
            time.sleep(2)
            
           
            if "404" not in driver.title and driver.current_url != "about:blank":
                print(f"Ссылка '{link_text}' кликабельна.")
            else:
                print(f"Ошибка: Ссылка '{link_text}' ведет на несуществующую страницу или пустую.")
                
            driver.back()
            time.sleep(2)
        
        except Exception as e:
            print(f"Ошибка при попытке кликнуть по ссылке '{link.text}': {e}")

finally:
  
    driver.quit()
