import scrapy
import csv
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class githubSpider(CrawlSpider):
	name = 'github_spider'

	start_urls = ['https://github.com/raokartikkumar24?tab=stars']

	rules = (Rule(LinkExtractor(allow=('/raokartikkumar24'),),callback='parse_page',follow=False),)

	def parse_page(self, response):
		print("parsing URL")
		print(response.url)
		csv_file = 'github_stars.csv'
		list_github_starts = response.css('div.d-inline-block > h3 > a::text').extract()
		if(len(list_github_starts) < 0):
			for s in list_github_starts:
				with open(csv_file, 'a+') as f:
					fwriter = csv.writer(f)
					csv.writerow(s)

