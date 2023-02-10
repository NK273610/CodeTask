from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Kunal is Bakchod'

@app.route('/mama', methods=['GET'])
def mama():
    return 'Mama is Bakchod'

if __name__== "__main__":
    app.run('localhost', 5000)