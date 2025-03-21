from flask import Flask, render_template, request
import os
import logging


logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nama = request.form['nama']
        pesan = request.form['pesan']
        return render_template('index.html', nama=nama, pesan=pesan)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
    