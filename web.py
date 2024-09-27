# Nikhil Khanchandani

from flask import Flask, render_template, request, redirect, url_for
from mastodon import Mastodon

app = Flask(__name__)

mastodon = Mastodon(
    access_token='lUR2Sy0nWAbwRiUryNM1_7yS3TJbfciHN21IJkMlKn4',
    api_base_url='https://mastodon.social'  # Change if needed
)

post_id = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global post_id
    if request.method == 'POST':
        if 'create' in request.form:
            status_text = request.form['status']
            post = mastodon.status_post(status_text)
            post_id = post['id']
        elif 'retrieve' in request.form:
            post = mastodon.status(post_id)
            return render_template('index.html', content=post['content'])
        elif 'delete' in request.form:
            mastodon.status_delete(post_id)
            post_id = None
            return render_template('index.html', content="Post deleted.")
    return render_template('index.html', content='')

if __name__ == '__main__':
    app.run(debug=True)
