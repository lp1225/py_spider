import requests
import re
import pickle


class SpiderSll:
    """
    爬取英雄信息
    """
    def __init__(self):
        self.base_url = "https://comp-sync.webapp.163.com/g78_pics/api?callback=jQuery111305605675268431101_1543719754263&_=1543719754264"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
                                        (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
        }
        self.hero_profile_url = []
        self.hero_biography = 'https://comp-sync.webapp.163.com/g78_hero/free_convey?callback=jQuery111302719748460647826_1543734429454&_=1543734429456'

    def send_request(self):
        response = requests.get(self.base_url, self.headers)
        data = response.content.decode('utf-8')
        result = re.findall('\((.*?)\)', data)
        result = result[0]
        result = result[29: -18]
        end_res = eval(result)
        print(end_res)
        return end_res

    def save_image(self, url_dict):
        """
        保存英雄图片
        :param url_dict:
        :return:
        """
        for key, value in url_dict.items():
            key_path_list = key.split('/')
            head_hero = key_path_list[-2]
            if head_hero == 'head_fang':
                print(head_hero)
                self.hero_profile_url.append(key_path_list[-1])
                key_path = ''.join(key_path_list)
                image_path = './image_sll/img_{}'.format(key_path)
                print(image_path)
                with open(image_path, 'wb') as f:
                    response = requests.get(value, self.headers)
                    f.write(response.content)
                    print(response)

    def save_profile_list(self):
        """
        保存图片list
        :return:
        """
        result = self.hero_profile_url
        pickle.dump(result, open('profile.txt', 'wb'))

    def run(self):
        url_dict = self.send_request()
        self.save_image(url_dict)
        print('===end===\n', url_dict)
        self.save_profile_list()


if __name__ == '__main__':
    SpiderSll().run()
