from lxml import etree
import requests


class SllImage:
    """
    爬取英雄图片
    """
    def __init__(self):
        self.base_url = 'http://moba.163.com/ssl/page.html?id=1003'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
                                (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
        }


    def send_request(self):
        response = requests.get(self.base_url, headers=self.headers)
        data = response.content.decode('utf-8')
        print(data)
        html = etree.HTML(data)
        res_list = html.xpath('//*[@id="acrobatics"]')
        print(res_list)
        res = etree.tostring(res_list[0]).decode()
        return res

    def run(self):
        data = self.send_request()
        print(data)


if __name__ == '__main__':
    SllImage().run()
