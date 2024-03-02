from flask import Flask

app = Flask(__name__)

@app.route('/')
def kaveriHello():
    return 'Hello Kaveri'

if __name__ == '__main__':
    app.run(debug=True)
