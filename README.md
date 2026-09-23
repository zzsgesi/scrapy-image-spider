# scrapy-image-spider

## 项目简介

基于 Scrapy 框架的图片批量采集系统，针对图片之家（tupianzj.com）的壁纸板块，实现从列表页到详情页的自动翻页爬取，并使用 ImagesPipeline 批量下载高清图片。

## 技术栈

- Python
- Scrapy
- ImagesPipeline
- XPath

## 功能说明

- 从列表页自动提取详情页链接，并构造高清图片页 URL
- 支持自动翻页，直到最后一页停止
- 使用 ImagesPipeline 批量下载图片，自动处理文件命名与存储
- 自定义请求头（User-Agent、Referer），降低被反爬拦截的风险
- 支持 Cookie 管理，应对需要登录或验证的页面


## 运行方式

1. 安装依赖：`pip install scrapy`
2. 进入项目目录：`cd tupian`
3. 运行爬虫：`scrapy crawl wenjian`
4. 图片会自动保存到 `./ceshitupian` 文件夹下

## 运行结果

成功爬取图片之家壁纸板块的图片，并通过 ImagesPipeline 批量下载到本地，支持自动翻页与断点续爬。
