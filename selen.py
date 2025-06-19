from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup


link = "https://letterboxd.com/films/popular/"

driver = Firefox()

driver.get(link)
sleep(2)

#element = driver.find_element(By.CSS_SELECTOR, "[data-film-slug]")

#attribute = element.__getattribute__('data-film-slug')
#print(attribute)


soup = BeautifulSoup(driver.page_source, "lxml")
print(soup.find('div', class_ = 'react-component poster film-poster barbie-heart linked-film-poster')['data-film-slug'])

driver.quit()
