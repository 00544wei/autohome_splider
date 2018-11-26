import scrapy
from autohome_splider.items import AutohomeSpliderItem

class AutoHomeSplider(scrapy.Spider):

    name = 'autohome_splider'

    allowed_domains = ['www.autohome.com.cn']

    start_urls = ['https://www.autohome.com.cn/shenzhen/']

    def parse(self, response):
        # response.xpath("")
        response.xpath("//div[@class='homepage-hotcar']/div[@class='hotcar-content']/div[@id='hotcar-2']/div[@class='list'][1]/div[@class='athm-slide js-hotcar-slide']/div[@class='athm-slide__inner']/ul[@class='athm-slide__track']//div[@class='box']/p[1]/a/@href").extract_first()

        print(response.text)