import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route("/get_prompt", methods=("POST",))
def generate_prompt():
    prompt = request.form.get('prompt')

    try:
        response = response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        response = f'''
        <div class="response-text"> {response.choices[0].text} </div>
        <hr/>
        '''
    except openai.error.RateLimitError:
        response = '''
        <div class="response-text" style="color: red;"> server overload please wait some minute and try again </div>
        <hr>
        '''
    
    return response

# app.run(debug=True)
