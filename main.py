from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = ‘<OPENAI-API-KEY’>

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    report_data = request.form['reportData']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the health report: {report_data}\nSummary:",
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
