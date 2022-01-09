import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from collections import OrderedDict
PATH="C:\\Users\\Shark\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe"
driver=webdriver.Chrome(PATH) 
driver.get("https://opensea.io/collection/capsulehouse?search[priceFilter][symbol]=ETH&search[priceFilter][max]=1.5&search[sortAscending]=false&search[sortBy]=LISTING_DATE&search[toggles][0]=BUY_NOW")
driver.maximize_window()
driver.implicitly_wait(2)

def func():
	idcapsules=[]
	driver.switch_to.window(driver.window_handles[0])
	driver.refresh()
	time.sleep(2.5)
	driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div[3]/div/div/div/div[2]/div/div/header/button/div[2]/i").click()
	for i in range (12):
		
		driver.execute_script("window.scrollTo(0, 700)") 
		x=driver.find_element_by_css_selector('div:nth-child('+str(i+7)+') .AssetCardFooter--name').text 
		y=driver.find_element_by_css_selector('div:nth-child('+str(i+7)+') .AssetCardFooter--price:nth-child(1) .Overflowreact__OverflowContainer-sc-10mm0lu-0:nth-child(2)').text
		real=int(x)-0
		if float(y)<.99:
			idcapsules.append(real)
			print(real,y)
			
		
		i=i+1
		
	return idcapsules

driver.execute_script("window.open('https://rarity.tools/capsulehouse?sort=priceLowHigh', 'tab2');")
driver.execute_script("window.open('https://messages.textfree.us/login', 'tab3');")
driver.switch_to.window("tab3")
driver.implicitly_wait(2)
driver.find_element_by_xpath("/html/body/div[1]/login-component/div/div[1]/div[2]/form/div[1]/input").send_keys("ethbeater")
driver.implicitly_wait(2)
driver.find_element_by_xpath("/html/body/div[1]/login-component/div/div[1]/div[2]/form/div[2]/div[1]/input").send_keys("Yeetyah1092")
driver.implicitly_wait(2)
driver.find_element_by_xpath("/html/body/div[1]/login-component/div/div[1]/div[2]/form/div[4]/button").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/pmk-add-google-contacts-modal/div[1]/div").click()

x=2
while x>0:
	length=func()
	driver.switch_to.window("tab2")
	driver.refresh() 
	time.sleep(2)
	for i in range(len(length)):
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
		driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/input[1]').clear()
		time.sleep(.2)
		driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/input[1]').clear()
		time.sleep(.2)
		driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/input[1]').clear()
		time.sleep(.4)
		driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/input[1]').send_keys(length[i])
		time.sleep(1)
		
		driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/input[2]').click()
		time.sleep(1.2)
		
		try:
			driver.implicitly_wait(5)
			rarity=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div[2]").text
		except NoSuchElementException:
			driver.refresh()
			time.sleep(4)
			driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/input[1]').send_keys(length[i])
			time.sleep(.5)
			driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/input[2]').click()
			rarity=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div[2]").text

		if float(rarity)<120:
			time.sleep(.5)
			webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
		else:
			link=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div[2]/div/div[1]/div/div[4]/a").get_attribute('href')
			driver.switch_to.window("tab3")
			driver.find_element_by_xpath("/html/body/div[1]/conversation-container/div/div/main/div[2]/ng-transclude/div/div[2]/conversation-input/form/div/div[2]/div[1]").send_keys("Sniper:ID#" ,length[i]," With "+str(rarity)+" Rarity.",link)
			driver.find_element_by_xpath("/html/body/div[1]/conversation-container/div/div/main/div[2]/ng-transclude/div/div[2]/conversation-input/form/button").click()






	