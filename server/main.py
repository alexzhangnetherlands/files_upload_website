from flask import Flask
app = Flask(__name__)

@app.route('/test')
def test():
    return 'test'

app.run(host='0.0.0.0', port=228)