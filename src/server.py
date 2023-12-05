from flask import Flask, render_template, request
from openai import OpenAI

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

# Replace YOUR_API_KEY with your OpenAI API key
client = OpenAI(api_key='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')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userprompt = request.form['prompt']

        client = OpenAI(api_key = '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')
        response = client.images.generate(
          model="dall-e-3",
          prompt=userprompt,
          size="1024x1024",
          quality="standard",
          style="vivid",
          n=1,
        )

        image_url = response.data[0].url

        return render_template('index.html', prompt=userprompt, image_url=image_url)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()