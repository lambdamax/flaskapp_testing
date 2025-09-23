import unittest
import requests
import threading
from flaskapp import app

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Start the Flask server in a new thread
        cls.server_thread = threading.Thread(target=cls.start_app)
        cls.server_thread.start()
        
        # Allow time for the server to start
        import time
        time.sleep(1)

    @classmethod
    def start_app(cls):
        app.run(debug=False, use_reloader=False)

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask server
        requests.post('http://127.0.0.1:5000/shutdown')  # We'll add this route to support clean shutdown
        cls.server_thread.join()

    def test_store_input(self):
        response = requests.post('http://127.0.0.1:5000/store', data={'input': 'Hello, World!'})
        self.assertEqual(response.text, "Input stored successfully!")

    def test_get_stored_input(self):
        # First, store some input
        requests.post('http://127.0.0.1:5000/store', data={'input': 'Hello, World!'})
        
        # Then, retrieve it
        response = requests.get('http://127.0.0.1:5000/get-stored-input')
        self.assertIn('Hello, World!', response.text)

    def test_reflected_xss(self):
        # Test for reflected XSS
        xss_input = '<script>alert("XSS")</script>'
        requests.post('http://127.0.0.1:5000/store', data={'input': xss_input})
        
        # Retrieve stored input
        response = requests.get('http://127.0.0.1:5000/get-stored-input')
        self.assertNotIn('<script>', response.text)  # Check that the response doesn't echo the script tag

if __name__ == '__main__':
    unittest.main()
