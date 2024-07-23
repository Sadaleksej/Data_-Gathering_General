import scrapy


class UnsplashPicSpider(scrapy.Spider):
    name = "unsplash_pic"
    start_urls = ["https://unsplash.com"]


    def parse(self, response):
        for image in response.xpath('//a[@itemprop="contentUrl"]/div/img[2]'):
            image_url = image.xpath("@src").extract_first() 
            name= image.xpath("@alt").extract_first()
            yield scrapy.Request(response.urljoin(image_url), self.save_image,  meta={'pic_name' : name})

    def save_image(self, response):
        name = response.request.meta['pic_name']
        with open(f'images/{name}'+'.jpg', 'wb') as f:
            f.write(response.body) 

           