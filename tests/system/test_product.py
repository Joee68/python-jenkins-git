import json
from unittest import TestCase

from mypage2 import app
import json
class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()),
                             [{"price":22000.5,"productId":1,"productName":"MI","rating":4.2},
                              {"price":115000.5,"productId":2,"productName":"Iphone","rating":4.3},
                              {"price":55000.5,"productId":3,"productName":"Oneplus","rating":4.1},
                              {"price":"23550","productId":"4","productName":"Xoami","rating":"4.0"}])
