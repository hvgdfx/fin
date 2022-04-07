from spider.spider.all_spider.base_spdier import BaseSpider


class ShSpider(BaseSpider):
    def get_urls(self):
        pass

    def parse_spidered_result(self):
        pass


if __name__ == '__main__':
    sh_spider = ShSpider("list_stock")
    sh_spider.schedule()
