# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# scrapy crawl wenjian

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class TupianPipeline:
    def process_item(self, item, spider):
        # 数据的存储
        return item


# 想要使用ImagesPipeline 必须单独设置一个配置 用来保存文件的文件夹（在settings里面加这个代码：IMAGES_STORE="./文件夹的名字"）
class meinvPipeline(ImagesPipeline):  # 继承scrapy本身就有的类 来帮我们下载图片
    def get_media_requests(self, item, info):  # 负责下载的
        yield scrapy.Request(
            url=item['img_src_1'],
            method='get',
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Referer": item['Referer']}
        )

    def file_path(self, request, response=None, info=None, *, item=None):  # 准备文件路径
        file_name = request.url.split('/')[-1]  # request.url可以直接获取到刚刚请求的url
        return f'img/{file_name}'

    def item_completed(self, results, item, info):  # 返回文件的详细信息
        print(results)
