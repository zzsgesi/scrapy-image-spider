import scrapy
from scrapy_playwright.page import PageMethod
from tupian.items import TupianItem


# scrapy crawl wenjian
class WenjianSpider(scrapy.Spider):
    name = "wenjian"
    start_urls = ["https://www.tupianzj.com/bizhi/DNmeinv/"]

    def start_requests(self):
        cookie_str = 't=132ce3f0b0160682f8285b40662370da; r=8081; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1772426591,1772445117,1772514467,1772529137; HMACCOUNT=6D111398433F299B; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1772531249'
        cookie_1 = cookie_str.split('; ')
        dic = {}  # 注意 cookie可能会变 如果爬取不到数据了 但是还没报错 就可能是cookie变了
        for it in cookie_1:
            k, v = it.split('=', 1)
            dic[k] = v
        yield scrapy.Request(
            url=self.start_urls[0],
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"},
            cookies=dic)

    def parse(self, resp, **kwargs):
        cookies_str = "t=2ed4de0df3521c1db4ac5fec34f2561e; r=3301; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1772426591,1772445117,1772514467,1772529137; HMACCOUNT=6D111398433F299B; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1772531304"
        cookies_1 = cookies_str.split('; ')
        dict = {}  # 注意 cookie可能会变 如果爬取不到数据了 但是还没报错 就可能是cookie变了
        for it in cookies_1:
            k, v = it.split('=', 1)
            dict[k] = v
        resp = resp.replace(encoding="gbk")
        li_list = resp.xpath('//*[@id="container"]/div/div/div[3]/div/ul/li')
        for li in li_list:
            href = li.xpath('./a/@href').extract_first()
            url_1 = resp.urljoin(href)
            url = url_1.replace('.html', '_2560x1600.html')
            yield scrapy.Request(
                url=url,
                method='get',
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
                , callback=self.parse_detail
                , cookies=dict)
        next_href = resp.xpath('//*[@class="pages"]/ul/li/a[contains(text(),"下一页")]/@href').extract_first()
        if next_href:
            yield scrapy.Request(
                url=resp.urljoin(next_href),
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"},
                cookies=dict,
                callback=self.parse)
        else:
            print("爬取完成 已经最后一页了")
        # meta={"playwright": True,
        # "playwright_page_methods": [PageMethod("wait_for_selector", '//*[@id="bigpic"]',timeout=10000)]
        #       })

    def parse_detail(self, resp, **kwargs):
        print(resp.url)
        resp = resp.replace(encoding="gbk")
        img_src_1 = resp.xpath('//div[@id="bigpic"]/a/img/@src').extract_first()
        tupian = TupianItem()
        tupian['img_src_1'] = img_src_1
        tupian['Referer'] = resp.url
        yield tupian
