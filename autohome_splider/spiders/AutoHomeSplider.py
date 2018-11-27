from telnetlib import EC

import scrapy
from autohome_splider.items import AutohomeSpliderItem
from selenium import webdriver
import selenium.webdriver.support.ui as ui

class AutoHomeSplider(scrapy.Spider):

    name = 'autohome_splider'

    allowed_domains = ['www.autohome.com.cn']
    # allowed_domains = ['www.baidu.com']

    start_urls = ['https://www.autohome.com.cn/shenzhen/']
    # start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        # response.xpath("")
        driver = webdriver.Chrome()
        # wait = ui.WebDriverWait(driver, 10)
        driver.get("https://www.autohome.com.cn/shenzhen/")
        driver.implicitly_wait(10)
        # wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']/div[@class='brand eye-protector-processed']/dl/dd"))
        selectBar = driver.find_element_by_xpath("/html[@class='eye-protector-processed']/body/div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__selected']").extract()
        print(selectBar)
        # brandList = driver.find_element_by_xpath("//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']/div[@class='brand eye-protector-processed']/dl/dd").extract()
        # print(brandList)
        # for i_brand in brandList:
        #     i_brandName = driver.find_element_by_xpath("//div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__selected']").extract().strip()
        #     print(i_brandName)

        # car_data_values = response.xpath("//div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']/div[@class='series eye-protector-processed show-animate']/dl[@class='list']/dd[2]/@data-value").extract()
        #
        # for i_data_value in car_data_values:
        #     print(i_data_value)

        # print(response.text)

    def waitClick(self, time, element):
        try:
            print('元素加载, 页面等待中 ...')
            ui.WebDriverWait(self.browser, time).until(EC.presence_of_element_located(element))
            self.browser.find_element(*element)
        except Exception as e:
            print('元素异常, 页面已截图 :')
            self.screenshot()