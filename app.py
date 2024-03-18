from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

def chat_with_api(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content" : prompt}]
    )

    return response.choices[0].message.content.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    response = chat_with_api(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
