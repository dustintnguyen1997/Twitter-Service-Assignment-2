# Chint Patel

import unittest
from unittest.mock import patch
from mastodon_service import create_post, retrieve_post, delete_post

class TestMastodonService(unittest.TestCase):

    @patch('mastodon_service.mastodon.status_post')
    def test_create_post(self, mock_status_post):
        # Mock the return value as a dictionary with both 'id' and 'content'
        mock_status_post.return_value = {'id': 123, 'content': 'Test Post'}
        
        # Call the function and unpack the returned values
        post_id, content = create_post("Test Post")
        
        # Validate the results
        self.assertEqual(post_id, 123)
        self.assertEqual(content, 'Test Post')

    @patch('mastodon_service.mastodon.status')
    def test_retrieve_post(self, mock_status):
        mock_status.return_value = {'id': 123, 'content': 'Test Post'}
        post_id, content = retrieve_post(123)
        self.assertEqual(post_id, 123)
        self.assertEqual(content, 'Test Post')

    @patch('mastodon_service.mastodon.status_delete')
    def test_delete_post(self, mock_status_delete):
        mock_status_delete.return_value = None
        result = delete_post(123)
        self.assertEqual(result, "Post 123 deleted.")

if __name__ == '__main__':
    unittest.main()