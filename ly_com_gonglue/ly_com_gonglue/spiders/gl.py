import scrapy


class GlSpider(scrapy.Spider):
    name = 'gl'
    # allowed_domains = ['gl.com']
    start_url = 'https://www.ly.com/travels/home/GetJingHuaYouJiListToIndex?pindex={}&psize=100&iid='
    art_url = 'https://www.ly.com/travels/{}.html'

    def start_requests(self):
        for page in range(1, 117):
            yield scrapy.Request(url=self.start_url.format(page))
            # break

    def parse(self, response):
        # print(response.json())
        resp_json = response.json()
        for one_art in resp_json['Obj']['YouJiList']:
            # print(one_art)
            travelNoteId = one_art['travelNoteId']
            # yield scrapy.Request(url=self.art_url.format(travelNoteId))
            one_art['article_url'] = self.art_url.format(travelNoteId)
            yield one_art