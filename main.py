from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from time import sleep
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)

driver.maximize_window()
driver.get("https://www.amazon.in/")