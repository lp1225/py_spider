import requests
import pickle


class SpiderList:
    """
    获取英雄信息列表
    """
    def __init__(self):
        self.hero_name = 'https://moba.res.netease.com/pc/zt/20171216152639/data/shishen.json'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
                                                (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
        }
        self.temp = {}

    def load_profile(self):
        res_list = pickle.load(open('profile.txt', 'rb'))

        return res_list

    def send_requests(self):
        """
        得到名字列表
        :return:
        """
        res_list = self.load_profile()
        for res in res_list:
            res_id = res.split('.')[0]
            response = requests.get(self.hero_name, self.headers)
            data = response.content.decode('utf-8')
            data = eval(data)

            for item in data:
                if res_id == str(item['id']):
                    self.temp[res_id] = {
                        'name': item['name'],
                        'image': res
                    }

    def save_hero(self):

        pickle.dump(self.temp, open('herolist.txt', 'wb'))

    def run(self):
        data = self.send_requests()
        self.save_hero()


if __name__ == '__main__':
    global null
    null = ''
    SpiderList().run()