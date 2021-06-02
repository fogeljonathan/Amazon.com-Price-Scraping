from selenium import webdriver
from datetime import datetime

subjecturl= 'https://www.amazon.com/Corsair-Vengeance-3200MHz-Desktop-Memory/dp/B0143UM4TC/ref=sr_1_2?crid=39Z7VBK29J1SD&dchild=1&keywords=corsair+vengeance+16gb&qid=1622609167&sprefix=Corsair+%2Caps%2C152&sr=8-2'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\CodeFiles\chromedriver.exe')
driver.get(subjecturl)

price=driver.find_element_by_xpath('//*[@id="price_inside_buybox"]').text

print("The price of 2x 8Gb Corsair Vengeance RAM on "+str(datetime.now())+" was: "+price+" USD.")
