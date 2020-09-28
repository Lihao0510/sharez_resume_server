import unittest
from app.service import user_service
from server import app
import json


def filter_func(item):
    return item % 2 == 0


class UserTest(unittest.TestCase):

    def setUp(self) -> None:
        # self.app = app
        # self.app.config['TESTING'] = True
        # self.client = app.test_client()
        pass

    def tearDown(self) -> None:
        pass

    def test_get_all_user(self):
        print('当前测试实例 ==>', self.client)
        response = self.client.get("user")
        resp_json = response.data
        # resp_dict = json.loads(resp_json)
        print('测试网络请求 ==>', resp_json)

    def test_create_user(self):
        print('当前测试实例 ==>', self)
        # user_service.get_all_user()
        self.assertIsNotNone(user_service)

    def test_filter(self):
        origin_list = [1, 3, 4, 5, 6, 8, 9]
        new_list = filter(filter_func, origin_list)
        print('过滤结果 ==>', list(new_list))
        self.assertIsNotNone(new_list)


if __name__ == '__main__':
    unittest.main()
