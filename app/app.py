from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vaccination_status', methods=['POST'])
def vaccination_status():
    regno = request.form['regno']
    response = requests.get(f'http://database:5001/vaccination_status/{regno}')
    vaccination_status = response.json()['vaccination_status']
    return render_template('vaccination_status.html', regno=regno, vaccination_status=vaccination_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
