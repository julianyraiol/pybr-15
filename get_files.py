import time

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.ui import Select

class IncraDriver(webdriver.Firefox, webdriver.Chrome, webdriver.Ie):

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.cities = []
        self.driver.get(url)
        
    def get_by_xpath(self, element):
        driver = self.driver
        select = Select(driver.find_element_by_xpath("//select[@name='" + element + "']"))
        return select

    def select_by_state(self, state):
        
        select = self.get_by_xpath("selectUf")
        select.select_by_visible_text(state)

    def select_by_city(self):
        driver = self.driver

        select = self.get_by_xpath("selectMunicipio")
        download = driver.find_element_by_id("botaoDownload")

        cities = [element.text for element in select.options]
        print(cities)

        for city in cities:
            select.select_by_visible_text(city)
            download.click()
            

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    incradriver = IncraDriver("https://sncr.serpro.gov.br/sncr-web/consultaPublica.jsf?windowId=997")
    incradriver.select_by_state('Amazonas')

    time.sleep(4)
    incradriver.select_by_city()