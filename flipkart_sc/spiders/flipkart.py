import scrapy
from flipkart_sc.items import FlipkartScItem

class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = ["https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"]

    def parse(self, response):
        items = FlipkartScItem()
        product_name = response.css('._4rR01T::text').extract()
        product_price = response.css('._1_WHN1::text').extract()
        product_ram_rom = response.css('.rgWa7D:nth-child(1)').css('::text').extract()
        product_bettry = response.css('.rgWa7D:nth-child(4)').css('::text').extract()
        product_imagelink = response.css('._396cs4::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_ram_rom'] = product_ram_rom
        items['product_bettry'] = product_bettry
        items['product_imagelink'] = product_imagelink
        yield items
