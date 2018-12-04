from flask import Flask
from api import api



app = Flask(__name__)
app.register_blueprint(api)
# 支持返回的jsonfy数据是中文
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
