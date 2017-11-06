# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class MyCrwalerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from scrapy.http import HtmlResponse
from selenium import webdriver


# class MeijuMiddleware(object):
#     def process_request(self, request, spider):
#         if spider.name == "ttmeiju":
#
#             spider.browser.get(request.url)
#             return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding='utf-8',
#                                 request=request)

class MeijuMiddleware(object):
    def process_request(self, request, spider):
        request_url = request.url
        if spider.name == "ttmeiju":
            # chrome_options = webdriver.ChromeOptions()
            # prefs = {"profile.managed_default_content_settings.images": 2}
            # # path = '/Users/canvas/project/seleniumdivers/chromedriver'
            # path = "E:/selenium_driver/chromedriver.exe"
            # chrome_options.add_experimental_option("prefs", prefs)
            # browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
            # print('请求')
            # browser = request.meta['browser']
            # browser.get(request.url)
            # return HtmlResponse(url=browser.current_url, body=browser.page_source, encoding='utf-8',
            #                     request=request)


            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            # path = '/Users/canvas/project/seleniumdivers/chromedriver'
            path = "E:/selenium_driver/chromedriver.exe"
            chrome_options.add_experimental_option("prefs", prefs)
            browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

            if request_url == "http://www.ttmeiju.vip/index.php/user/login.html":
                browser.get(request_url)
                spider.browser = browser
                return HtmlResponse(url=browser.current_url, body=browser.page_source, encoding='utf-8',
                                    request=request)
            else:
                cookies = spider.web_cookies
                print(cookies[0])

                browser.add_cookie(cookies[0])

                browser.get(request_url)
                spider.browser = browser
                return HtmlResponse(url=browser.current_url, body=browser.page_source, encoding='utf-8',
                                    request=request)
