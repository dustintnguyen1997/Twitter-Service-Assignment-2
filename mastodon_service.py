# Dustin Nguyen


from mastodon import Mastodon

# Initialize Mastodon client
mastodon = Mastodon(
    access_token='lUR2Sy0nWAbwRiUryNM1_7yS3TJbfciHN21IJkMlKn4',
    api_base_url='https://mastodon.social'  # Change to your instance if different
)

# Create a new post
def create_post(status_text):
    post = mastodon.status_post(status_text)
    return post['id'], post['content']

# Retrieve a post
def retrieve_post(post_id):
    post = mastodon.status(post_id)
    return post['id'], post['content']

# Delete a post
def delete_post(post_id):
    mastodon.status_delete(post_id)
    return f"Post {post_id} deleted."

if __name__ == "__main__":
    # Example Usage:
    post_id, content = create_post("Hello Mastodon!")
    print(f"Created Post: {content}")

    retrieved_id, retrieved_content = retrieve_post(post_id)
    print(f"Retrieved Post: {retrieved_content}")

    delete_message = delete_post(post_id)
    print(delete_message)