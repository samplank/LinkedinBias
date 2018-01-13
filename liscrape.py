import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import minnesota

zipped = zip(minnesota.names,minnesota.pages)

for tup in zipped:

	number = 0
	page = tup[1]
	driver = webdriver.Firefox()
	driver.get(page)
	
	# 1. get page HTML as string
	pghtml = driver.page_source


	# 2. parse page with beautiful soup
	soup = BeautifulSoup(pghtml, "html.parser")

	# 3. iterate through image links and save them 

	newdir = '/Users/samplank/Desktop/gov2430photos/' + tup[0]
	
	if not os.path.exists(newdir):
		os.makedirs(newdir)
	

	for x in soup.find_all(class_="browse-map"):
		for y in x.find_all(class_="info"):
			for z in y.find_all('a', href=True):
				outlink = z['href']
				driver2 = webdriver.Firefox()
				driver2.get(outlink)
				driver2.get_screenshot_as_file(newdir + '/' + str(number) + '.png')
				driver2.close()
				number = number + 1


	#for profile in soup.select('#aux > div.insights > div.insights-browse-map > ul > li > a'):
		#print(profile)

	driver.close()
