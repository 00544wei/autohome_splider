import time
from telnetlib import EC

import scrapy
from selenium.webdriver.support.select import Select

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
        #定位到汽车之家首页的下拉框处 并触发点击事件
        driver.find_element_by_xpath("//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__selected']/span[@class='athm-select__icon']/i[@class='athm-iconfont athm-iconfont-arrowdown']").click()
        #获取点击下拉框之后出现的下拉框值
        select = driver.find_element_by_xpath("//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']//div[1]")
        # print(driver.page_source)
        #获取所有的dd元素  （品牌信息包含在里面）
        options = select.find_elements_by_tag_name("dd")
        i = 1
        y = 1
        for i_option in options:
            #拼接一级标签的xpath路径
            i_path = "//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']//div[1]/dl/dd[" + str(i)+ "]"
            i += 1
            print(i_path)
            print(i_option.text)
            #根据拿到的一级标签的xpath路径进行点击操作  以便获取二级标签的内容
            select.find_element_by_xpath(i_path).click()
            second_select = select.find_element_by_xpath("//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']//div[2]/dl")
            second_options = second_select.find_elements_by_tag_name("dd[]")
            for i_second_option in second_options:
                if y == 1:
                    continue
                print(i_second_option.text)
            # print(i_option.get_attribute("data-value"))
        # selectValues = driver.find_element_by_xpath("//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']/div[@class='brand eye-protector-processed']/dl/dd")
        # sel = Select(selectValues)
        # allOptions = sel.options
        # print(allOptions)
        # print(response.text)

    def waitClick(self, time, element):
        try:
            print('元素加载, 页面等待中 ...')
            ui.WebDriverWait(self.browser, time).until(EC.presence_of_element_located(element))
            self.browser.find_element(*element)
        except Exception as e:
            print('元素异常, 页面已截图 :')
            self.screenshot()