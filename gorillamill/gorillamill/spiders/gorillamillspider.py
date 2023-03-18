# import csv
# import scrapy
# import pandas as pd

# class GorillaMillSpider(scrapy.Spider):
#     name = "gorillamill"
#     allowed_domains = ["gorillamill.com"]
    

#     def start_requests(self):
#         with open("Gorilla-Mill-Products.csv", 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 try:
#                     product_id = row[0]
#                     url = f"https://gorillamill.com/products/product/{product_id}"
#                 except:
#                     product_id = 'Id not working'
#                 yield scrapy.Request(url, self.parse)

#     def parse(self, response):
        
#         item = {}
       
#         item['id'] = response.css('a[data-product]::attr(data-product)').get()
#         item['title'] = " ".join(response.css('div#specs h2::text, h2::text, h1::text').getall())
#         item['data stuck'] = response.css('a[data-stock]::attr(data-stock)').get()
#         item['url'] = response.url
#         print(item)
#         yield item



# import csv
# import os
# import scrapy
# import pandas as pd

# class GorillaMillSpider(scrapy.Spider):
#     name = "gorillamill"
#     allowed_domains = ["gorillamill.com"]

#     def start_requests(self):
#         with open("Gorilla-Mill-Products.csv", 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 try:
#                     product_id = row[0]
#                     url = f"https://gorillamill.com/products/product/{product_id}"
#                 except:
#                     product_id = 'Id not working'
#                 yield scrapy.Request(url, self.parse)

#     def parse(self, response):
#         item = {}
#         item['id'] = response.css('a[data-product]::attr(data-product)').get()
#         item['title'] = " ".join(response.css('div#specs h2::text, h2::text, h1::text').getall())
#         item['data stuck'] = response.css('a[data-stock]::attr(data-stock)').get()
#         item['url'] = response.url
#         yield item


import csv
import os
import scrapy
import pandas as pd

class GorillaMillSpider(scrapy.Spider):
    name = "gorillamill"
    allowed_domains = ["gorillamill.com"]

    def start_requests(self):
        with open("Gorilla-Mill-Products.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    product_id = row[0]
                    url = f"https://gorillamill.com/products/product/{product_id}"
                except:
                    product_id = 'Id not working'
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        
        # item['id'] = response.css('a[data-product]::attr(data-product)').get()
        title = " ".join(response.css('div#specs h2::text, h2::text, h1::text').getall())
        # item['data stuck'] = response.css('a[data-stock]::attr(data-stock)').get()
        # item['url'] = response.url
        
        return {
            "title": title
        }
    
