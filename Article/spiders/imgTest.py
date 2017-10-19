# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from Article.items import ImgTestItem, ArticleItemLoader, ImgTestItemLoader
from scrapy.http import Request

from Article.utils.common import get_md5


class ImgtestSpider(scrapy.Spider):
    name = 'imgTest'
    # allowed_domains = ['http://www.mmonly.cc']
    # start_urls = ['http://www.mmonly.cc/wmtp/list_20_2.html']

    # def parse(self, response):
    #     img_nodes = response.css("#infinite_scroll div[class='item masonry_brick masonry-brick']")
    #     for img_node in img_nodes:
    #         front_image_url = img_node.css("img::attr(src)").extract_first("")
    #         img_item = ArticleItem()
    #         img_item["front_image_url"] = [front_image_url]
    #         print(front_image_url)
    #         yield img_item
    #     pass
    allowed_domains = ['http://1024.xtv919.com/pw']
    start_urls = ['http://1024.xtv919.com/pw/thread.php?fid=14']
    i = 2

    def parse(self, response):
        post_nodes = response.css('tbody h3')
        for post_node in post_nodes:
            post_url = post_node.css("a::attr(href)").extract_first("")
            if 'htm_data' in post_url:
                yield Request(url=parse.urljoin(response.url, post_url),
                              callback=self.parse_detail, dont_filter=True)
        next_url = "thread.php?fid=15&page=" + str(self.i)
        self.i += 1
        if next_url:
            print("next_url" + next_url)
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse, dont_filter=True)
        pass

    def parse_detail(self, response):
        title = response.css("#subject_tpc::text").extract()[0]
        url = response.url
        print(url)
        url_object_id = get_md5(url)
        image_nodes = response.css("#read_tpc a")
        image_urls = []
        img_item = ImgTestItem()
        for image_node in image_nodes:
            image_url = image_node.css("img::attr(src)").extract_first("")
            image_urls.append(image_url)
            # print(image_url)
        # img_item['image_urls'] = image_urls
        # img_item['title'] = title
        # img_item['url'] = url
        # img_item['url_object_id'] = url_object_id

        item_loader = ImgTestItemLoader(item=ImgTestItem(), response=response)
        item_loader.add_value('image_urls', image_urls)
        item_loader.add_value('url_object_id', url_object_id)
        item_loader.add_value('title', title)
        item_loader.add_value('url', url)
        img_item = item_loader.load_item()
        yield img_item
