# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import re
from scrapy.loader import ItemLoader
from my_crwaler.items import TtmeijuItem
import my_crwaler.utils.common as utils


class TtmeijuSpider(scrapy.Spider):
    name = 'ttmeiju'
    allowed_domains = ['www.ttmeiju.vip']
    start_urls = ['http://www.ttmeiju.vip/index.php/user/login.html']
    login_user = 'canvas0607'
    login_pwd = 'tusbasa1'

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        'Accept-Language': "zh-CN,zh;q=0.8,en;q=0.6",
        "Host": "www.ttmeiju.vip"
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, callback=self.is_login)

    def is_login(self, response):
        login_flag = response.css('#loginform')
        if login_flag is not None:
            # 登录
            params = {
                'username': self.login_user,
                'password': self.login_pwd
            }
            return [scrapy.FormRequest(
                url=self.start_urls[0],
                formdata=params,
                headers=self.headers,
                callback=self.check_login
            )]

    def check_login(self, response):
        # 成功之后请求列表页
        url = 'http://www.ttmeiju.vip/summary.html'
        yield scrapy.Request(url=url, dont_filter=True, headers=self.headers)

    def parse(self, response):
        # 解析分页 .pagination .num
        detail_urls = response.css('.latesttable a::attr(href)').extract()
        detail_pattern = "^/meiju/[^(Movie.html)]"
        for detail_url in detail_urls:
            if re.match(detail_pattern, detail_url, flags=0):
                real_detail_url = parse.urljoin(response.url, detail_url)
                yield scrapy.Request(real_detail_url, headers=self.headers, callback=self.detail_parse)

        page_urls = response.css('.pagination .num::attr(href)').extract()
        for page_url in page_urls:
            real_url = parse.urljoin(response.url, page_url)
            yield scrapy.Request(real_url, headers=self.headers)

    def detail_parse(self, response):
        # 详细链接列表
        seed_lists = response.css('#seedlist tr')
        for seed_list in seed_lists:
            tmp_urls = {"baidu": "null", "bt": "null", "xunlei": "null", "xiaomi": "null", "ed2": "null"}
            title = seed_list.css("td a").extract_first()

            dr = re.compile(r'<[^>]+>', re.S)
            dd = dr.sub('', title)
            dd = dd.replace('\t', "").replace('\n', "")
            # 数据库主键
            object_id = utils.get_md5(dd)
            # x = dd
            title_list = dd.split(" ")
            # 获取中文标题
            chinese_title = title_list[0]
            eposode_info = ""
            for info in title_list:
                if re.match("S\d+E\d+", info):
                    eposode_info = info
            eposode_position = title_list.index(eposode_info)
            # 获取集的信息
            english_split = title_list[1:eposode_position]
            # 由于英文有空格 切片链接
            english_title = " ".join(english_split)
            eposode_list = re.search(r"S(\d+)E(\d+)", eposode_info)
            season = eposode_list.group(1)
            episode = eposode_list.group(2)
            seed_list_urls = seed_list.css('td ::attr(href)').extract()
            for seed_list_url in seed_list_urls:
                if re.match("^https://pan.baidu.com*", seed_list_url, flags=0):
                    tmp_urls['baidu'] = seed_list_url
                if re.match("^https://rarbg.is/download.php*", seed_list_url, flags=0):
                    tmp_urls['bt'] = seed_list_url
                if re.match("^magnet:\?xt=urn:btih*", seed_list_url, flags=0):
                    tmp_urls['xunlei'] = seed_list_url
                if re.match("^https:d.miwifi.com*", seed_list_url, flags=0):
                    tmp_urls['xiaomi'] = seed_list_url
                if re.match("^ed2k://*", seed_list_url, flags=0):
                    tmp_urls['ed2'] = seed_list_url

            decribes = seed_list.css('td::text').extract()
            subtitles = seed_list.css('td font::text').extract()
            subtitle = '无字幕'
            for subtitle in subtitles:
                if "内嵌双语字幕" in subtitle:
                    subtitle = "内嵌双语字幕"
            additional_descs = {'subtitle': subtitle, "size": "null", "kind": "null", "release_time": "null"}
            for decribe in decribes:
                # 匹配大小
                if re.match("(^\d+M$)|(^\d+(\.\d+)G$)", decribe, flags=0):
                    additional_descs['size'] = decribe
                # 匹配类型
                if re.match("普清|熟肉|(^\d+p$)", decribe, flags=0):
                    additional_descs['kind'] = decribe
                if re.match("\d{4}-\d{2}-\d+", decribe, flags=0):
                    additional_descs['release_time'] = decribe
            item_loader = ItemLoader(item=TtmeijuItem(), response=response)
            item_loader.add_value("describes", additional_descs)
            item_loader.add_value("urls", tmp_urls)
            item_loader.add_value("title", dd)
            item_loader.add_value("baiduUrl", tmp_urls.get('baidu'))
            item_loader.add_value("xunleiUrl", tmp_urls.get('xunlei'))
            item_loader.add_value("xiaomiUrl", tmp_urls.get('xiaomi'))
            item_loader.add_value("ed2Url", tmp_urls.get('ed2'))
            item_loader.add_value("btUrl", tmp_urls.get('bt'))
            item_loader.add_value("kind", additional_descs.get('kind'))
            item_loader.add_value("size", additional_descs.get('size'))
            item_loader.add_value("release_time", additional_descs.get('release_time'))
            item_loader.add_value("subtitle", additional_descs.get('subtitle'))
            item_loader.add_value("chinese_title", chinese_title)
            item_loader.add_value("english_title", english_title)
            item_loader.add_value("season", season)
            item_loader.add_value("episode", episode)
            item_loader.add_value("object_id", object_id)
            yield item_loader.load_item()