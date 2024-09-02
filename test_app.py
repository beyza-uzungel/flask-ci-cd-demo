import unittest
from app import app, db, Message

class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.client = app.test_client()
        cls.client.testing = True
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.drop_all()

    def test_home_page_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Selam ! Burası Test Ortamıdır.', response.data.decode('utf-8'))

    def test_post_message(self):
        response = self.client.post('/', data={'content': 'Test Message'})
        self.assertEqual(response.status_code, 302)  # Redirect after post
        with app.app_context():
            message = Message.query.filter_by(content='Test Message').first()
            self.assertIsNotNone(message)
            self.assertEqual(message.content, 'Test Message')

if __name__ == '__main__':
    unittest.main()
