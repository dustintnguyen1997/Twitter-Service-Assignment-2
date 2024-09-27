from mastodon import Mastodon

Mastodon.create_app(
    'Twitter Service',
    api_base_url='https://mastodon.social/',
    to_file='Ci1pe__LrkxaL-X6g1XZe_AzfHQrESjkmJ6M9POD5Gg'
)


mastodon = Mastodon(client_id='Ci1pe__LrkxaL-X6g1XZe_AzfHQrESjkmJ6M9POD5Gg', api_base_url='https://mastodon.social')

mastodon.log_in(
    'dustintnguyen1997@gmail.com',
    'mydestiny1',
    to_file='Ci1pe__LrkxaL-X6g1XZe_AzfHQrESjkmJ6M9POD5Gg'
)

def create_post(content):
    try:
        # Create a new status post
        status = mastodon.status_post(content)
        print(f"Post created with ID: {status['id']}")
        return status['id']  # Return the post ID for future retrieval
    except Exception as e:
        print(f"Error creating post: {e}")
        return None

def retrieve_post(post_id):
    try:
        # Retrieve the status by ID
        status = mastodon.status(post_id)
        print(f"Post retrieved: {status['content']}")
        return status['content']
    except Exception as e:
        print(f"Error retrieving post: {e}")
        return None

def delete_post(post_id):
    try:
        # Delete the status
        mastodon.status_delete(post_id)
        print(f"Post with ID {post_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting post: {e}")


if __name__ == "__main__":
    # Step 1: Create a post
    post_id = create_post("Hello from the Mastodon API!")

    if post_id:
        # Step 2: Retrieve the created post
        retrieved_content = retrieve_post(post_id)
        print(f"Retrieved content: {retrieved_content}")

        # Step 3: Delete the post
        delete_post(post_id)
