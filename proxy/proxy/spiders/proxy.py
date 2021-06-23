import scrapy
import re
from myproject.items import ProxyItem


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/']
    for i in range(2, 10):
        start_urls.append(f'https://www.kuaidaili.com/free/inha/{i}/')

    def parse(self, response):
        item = ProxyItem()
        ip = response.xpath('//tr/td[@data-title="IP"]/text()').extract()
        port = response.xpath('//tr/td[@data-title="PORT"]/text()').extract()
        area = response.xpath('//tr/td[@data-title="位置"]/text()').extract()
        for i in range(len(area)):
            if '省' in area[i]:
                area[i] = re.findall('(.*)省', area[i])[0]
            else:
                area[i] = re.findall('\s(.*?)\s', area[i])[0]
        types = response.xpath('//tr/td[@data-title="类型"]/text()').extract()
        for i in range(len(ip)):
            item['ip'] = ip[i]
            item['port'] = port[i]
            item['area'] = area[i]
            item['types'] = types[i]
            yield item
