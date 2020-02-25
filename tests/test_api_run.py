import time
import unittest

from app.interface.web import create_app
from app.infrastructure.config import TestConfig


class TestApiRun(unittest.TestCase):
    def setUp(self):
        print('Begin test api run')
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        print('End test api run')
        self.app_context.pop()

    @staticmethod
    def get_headers():
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_api_run(self):
        rv = self.client.get('/api/v1/run', headers=self.get_headers())
        print(rv.json)
        self.assertEqual('launching', rv.json['response'])
        self.assertEqual(202, rv.status_code)
        url = rv.__dict__['headers']['Location']
        print(url)
        time.sleep(1)
        rv = self.client.get(url, headers=self.get_headers())
        print(rv.json)
        url_kill = rv.__dict__['headers']['Kill']
        print(url_kill)
        i = 0
        while True:
            time.sleep(0.2)
            rv = self.client.get(url, headers=self.get_headers())
            print(rv.json)
            i += 1
            if i == 15:
                rv = self.client.get(url_kill, headers=self.get_headers())
                break



if __name__ == '__main__':
    unittest.main(verbosity=2)
