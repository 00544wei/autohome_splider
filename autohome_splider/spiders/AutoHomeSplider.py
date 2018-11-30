import time
from telnetlib import EC

import scrapy
from selenium.webdriver import ActionChains
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
        allSeriesUrls = self.get_crawl_series_list()
        # print(response.text)
        for i_series_url in allSeriesUrls:
            print(i_series_url)

    def get_crawl_series_list(self):
        # 用来存放所有要抓取的url （某一车系的url的地址）
        allSeriesUrls = []
        # response.xpath("")
        driver = webdriver.Chrome()
        # wait = ui.WebDriverWait(driver, 10)
        driver.get("https://www.autohome.com.cn/shenzhen/")
        driver.implicitly_wait(20)
        # 定位到汽车之家首页的下拉框处 并触发点击事件
        driver.find_element_by_xpath(
            "//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__selected']/span[@class='athm-select__icon']/i[@class='athm-iconfont athm-iconfont-arrowdown']").click()
        # 获取点击下拉框之后出现的下拉框值
        select = driver.find_element_by_xpath(
            "//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']//div[1]")
        # print(driver.page_source)
        # 获取所有的dd元素  （品牌信息包含在里面）
        options = select.find_elements_by_tag_name("dd")
        i = 1
        for i_option in options:
            # 拼接一级标签的xpath路径
            i_path = "//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']//div[1]/dl/dd[" + str(
                i) + "]"
            i += 1
            # 根据拿到的一级标签的xpath路径进行点击操作  以便获取二级标签的内容
            select.find_element_by_xpath(i_path).click()
            # 定位到二级标签的位置
            second_select = select.find_element_by_xpath(
                "//div[@class='wrapper']/div[@class='homepage-findcar']/div[@class='findcar-select']/div[@class='option option-brand']/div[@id='js-carpicker-brand1']/div[@class='athm-select__option']/div[@class='pop-wrapper']//div[2]/dl")
            # 获取到当前二级标签下所有的选项
            second_options = second_select.find_elements_by_tag_name("dd")
            pvareaid = ""
            for i_second_option in second_options:
                # 当二级标签的内容为“全部车系”的时候，取出 pvareaid
                if i_second_option.text == '全部车系':
                    alabel = second_select.find_elements_by_tag_name("a")
                    pvareaidstr = alabel[0].get_attribute("href")
                    brandUrlList = pvareaidstr.split("pvareaid=")
                    pvareaid = brandUrlList[1]
                    print(pvareaid)
                print(i_second_option.text)

                # 拼接要抓取的车系的url
                if str(i_second_option.get_attribute("data-value")) and str(pvareaid):
                    i_series_url = "https://car.autohome.com.cn/price/series-" + str(i_second_option.get_attribute("data-value")) + ".html#pvareaid=" + str(pvareaid)
                    allSeriesUrls.append(i_series_url)
                # ActionChains(driver).click_and_hold(i_second_option).perform()
                # ActionChains(driver).click_and_hold(i_second_option).release()
        return allSeriesUrls

    def waitClick(self, time, element):
        try:
            print('元素加载, 页面等待中 ...')
            ui.WebDriverWait(self.browser, time).until(EC.presence_of_element_located(element))
            self.browser.find_element(*element)
        except Exception as e:
            print('元素异常, 页面已截图 :')
            self.screenshot()