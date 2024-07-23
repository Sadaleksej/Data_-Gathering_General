import scrapy


class UnsplashPicSpider(scrapy.Spider):
    name = "unsplash_pic"
    start_urls = ["https://unsplash.com"]


    def parse(self, response):
        for image in response.xpath('//a[@itemprop="contentUrl"]/div/img[2]'):
            image_url = image.xpath("@src").extract_first() 
            yield scrapy.Request(response.urljoin(image_url), self.save_image)

    def save_image(self, response):
        filename = response.url.split('/')[-1]
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body) 