from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

url = "https://api.apilayer.com/email_verification/check?email="
api_key = "PUT YOUR KEY HERE"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/verify-email', methods=['POST'])
def verify_email():
    email = request.form.get('email')
    api_url = url + email
    headers = {"apikey": api_key}
    response = requests.get(api_url, headers=headers)
    status_code = response.status_code
    result = response.json()
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
