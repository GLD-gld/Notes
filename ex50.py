#你的第一个网站
# 安装flask
 pip install flask

#项目名 gothonweb
#发生了什么
1.浏览器建立了到你计算机的网络连接，可以使用localhost访问，它使用的网络端口是5000
2.连接成功以后，浏览器对app.py这个应用程序发出来HTTP请求（request），要求访问的URL为/，这通常是第一个网站的第一个URL。
3.既然flask找到了def index，它就调用了这个函数来处理请求，该函数运行后返回了一个字符串，以供flask将其传递给浏览器。
4.最后，flask完成了对浏览器请求的处理，将响应（response）回传给浏览器，于是你就看到了现在的页面。

#调试模式运行flask
export FLASK_DEBUG=1
