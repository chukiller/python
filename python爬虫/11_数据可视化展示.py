from flask import Flask, render_template

# 创建一个app
app = Flask(__name__)


# 准备一个函数处理浏览器发送的请求
@app.route("/")
def show():
    return render_template('show.html')


# 运行这个app
if __name__ == '__main__':
    app.run()
