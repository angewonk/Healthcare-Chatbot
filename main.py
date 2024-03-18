from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

def is_healthcare_prompt(prompt):
    healthcare_keywords = ["health", "medical", "doctor", "hospital", "medicine", "patient", "treatment", "symptom"]
    for keyword in healthcare_keywords:
        if keyword in prompt.lower():
            return True
    return False

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
    user_message = request.form['message']
    if is_healthcare_prompt(user_message):
        chatbot_response = chat_with_api(user_message)
    else:
        chatbot_response = "Please ask a healthcare-related question."
    return jsonify({"message": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
