from flask import Flask
import pandas as pd


app = Flask(__name__)


@app.route('/')
def hello_world():
    df = pd.DataFrame({'one':[1,2,3]})
    print('Мф ынесли изменения forWork')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
