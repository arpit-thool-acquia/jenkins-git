from app import app
import unittest
import requests

class FlaskTestCase(unittest.TestCase):

    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)


    def test_app_up(self):
        self.assertEqual(requests.get("http://localhost:5000/").status_code, 200)

    def test_input_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Road Type' in response.data)

    def test_history_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/history', content_type='html/text')
        self.assertTrue(b'Travel History' in response.data)

    def test_correct_input(self):
        tester = app.test_client(self)
        response = tester.post(
            '/',
            data=dict(road_type="urban", road_length="900"),
            follow_redirects=True
        )
        self.assertIn(b"Total Distance Travelled", response.data)

    def test_negative_input(self):
        tester = app.test_client(self)
        response = tester.post(
            '/',
            data=dict(road_type="urban", road_length="-32"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 500)

    def test_empty_input(self):
        tester = app.test_client(self)
        response = tester.post(
            '/',
            data=dict(road_type="urban", road_length="  "),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 500)
    

if __name__ == '__main__':
    unittest.main()