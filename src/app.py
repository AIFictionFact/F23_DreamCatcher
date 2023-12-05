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

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant that gives users accurate dream interpretations."},
                      {"role": "user", "content": userprompt}]
        )

        chat_response = completion.choices[0].message

        #print(chat_response)

        return render_template('index.html', prompt=userprompt, image_url=image_url, chat_response=chat_response.content)


        # return render_template('index.html', prompt=userprompt, image_url=image_url)

        # completion = client.chat.completions.create(    
        #     model="gpt-3.5-turbo",
        #     messages=userprompt
        # )

        # print(completion.choices[0].message)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#@app.route('/feedback')
#def about():
#   return render_template('feedback.html')

#@app.route('/login')
#def about():
#    return render_template('login.html')



if __name__ == '__main__':
    app.run()


#     from flask import Flask, render_template
# app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template('index.html')
# if __name__ == '__main__':
#    app.run()


# from openai import OpenAI
# import webbrowser
# import os

# # Replace YOUR_API_KEY with your OpenAI API key
# client = OpenAI(api_key = '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')
# response = client.images.generate(
#   model="dall-e-3",
#   prompt="I dreamt that I was sitting on a cloud and out of the blue I was falling and I landed on my office job at my desk with loads of work to do.",
#   size="1024x1024",
#   quality="standard",
#   style="natural",
#   n=1,
# )

# # TODO: use Flask framework to get get and post information to website so user can input prompt
# webbrowser.open(response.data[0].url)