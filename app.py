from book import create_app

app=create_app()

app.config["JSON_AS_ASCII"] = False
@app.route('/')
def hello_world():  # 测试flask启动状态
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

