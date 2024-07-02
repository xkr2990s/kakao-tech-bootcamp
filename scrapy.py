import scrapy

from scrapy import Spider

class WikiSpider(Spider):
  name = "wiki"
  
  def start_requests(self):
    url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD"
    yield scrapy.Request(url, self.parse_start)
    
  def parse(self, response):
    result = response.css('p').getall()
    
    for paragraph in result:
      self.log(paragraph)
    