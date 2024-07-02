import scrapy
from scrapy.crawler import CrawlerProcess

class WikiSpider(scrapy.Spider):
  name = "wiki"
  start_urls = ["https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD",]
    
  def parse(self, response):
    # 주요 콘텐츠를 가져옴
    content_div = response.css("#mw-content-text")
    # 텍스트를 모두 가져와서 리스트로 만듦
    paragraphs = content_div.css("p ::text").getall()
    # 텍스트 리스트를 하나의 문자열로 합침
    content = ' '.join(paragraphs).strip()
    
    yield {
      'content': content
    }