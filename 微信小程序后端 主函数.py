# coding: utf-8

import os
from io import BytesIO
import os,base64
from leancloud import Query
from leancloud import Object
from flask import Flask
from flask import redirect
from flask import url_for
from flask import g
from flask import request
from flask import send_from_directory
from flask import flash,make_response,Response  
from flask import Markup
from flask import render_template
from werkzeug import Request
import leancloud
import requests
import json,random
from views.todos import todos_view
from views.users import users_view
from aip import AipImageClassify
from aip import AipFace
from aip import AipBodyAnalysis
from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '11470546'
API_KEY = 'hBYWy8rqaABMrkKCdFpNqOaj'
SECRET_KEY = 'Eox3cFvvj2oV0I6OHqufUt4b7yfdYfyK '
client_ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
client_face = AipFace(APP_ID, API_KEY, SECRET_KEY)
client_count = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
app = Flask(__name__)
app.config.update(dict(PREFERRED_URL_SCHEME='https'))
try:
    app.secret_key = bytes(os.environ.get('SECRET_KEY'), 'utf-8')
except TypeError:
    import sys
    sys.exit('未检测到密钥。请在 LeanCloud 控制台 > 云引擎 > 设置中新增一个名为 SECRET_KEY 的环境变量，再重试部署。')
global cookie_data
cookie_data = "mmsess=s%3A70opOTJ-kIHh0aI_RT3RJEOgM5xBwSZr.r2sEk%2BF%2FWID8qnVZomBfKI7U2pmmhHRYgBnzZeAaeR0"
class Todo(Object):
    pass
class HTTPMethodOverrideMiddleware(object):
    """
    使用中间件以接受标准 HTTP 方法
    详见：https://gist.github.com/nervouna/47cf9b694842134c41f59d72bd18bd6c
    """

    allowed_methods = frozenset(['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
    bodyless_methods = frozenset(['GET', 'HEAD', 'DELETE', 'OPTIONS'])

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        method = request.args.get('METHOD', '').upper()
        if method in self.allowed_methods:
            method = method.encode('ascii', 'replace')
            environ['REQUEST_METHOD'] = method
        if method in self.bodyless_methods:
            environ['CONTENT_LENGTH'] = 0
        return self.app(environ, start_response)

# 注册中间件
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
app.wsgi_app = leancloud.HttpsRedirectMiddleware(app.wsgi_app)
app.wsgi_app = leancloud.engine.CookieSessionMiddleware(app.wsgi_app, app.secret_key)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')
app.register_blueprint(users_view, url_prefix='/users')






@app.route('/')
def index():
    return redirect(url_for('todos.show'))

def Response_headers(content):  
    resp = Response(content)  
    resp.headers['Access-Control-Allow-Origin'] = '*'  
    return resp 
@app.route('/help')
def help():
    Todo = Object.extend('Todo')
    query = Query(Todo)

    query.equal_to('sent', "0")
    gameScores = query.find()
    print (gameScores)
    

    

    return render_template('help.html')

@app.route('/cookie',methods=['GET','POST'])
def cookie(): 
        global cookie_data
        print(request.form)
        print(request.form.to_dict())
        cookie_data = request.form.to_dict()['cookie']
        print (cookie_data) 
        return "New cookie :" + cookie_data

@app.route('/count',methods=['GET','POST'])
def count():
    print(request.form)
    url = request.form.to_dict()['url']
    print(url)
    response = requests.get(url)
    # 将这个图片从内存中打开，然后就可以用Image的方法进行操作了
    options = {}
    options["show"] = "true"
    """ 带参数调用人流量统计 """
    result =client_count.bodyNum(BytesIO(response.content).read(), options)
    #print("Result:  "+ str(result))
    return str(result).replace("\'","\"")



@app.route('/face',methods=['GET','POST'])
def face():
    print(request.form)
    url = request.form.to_dict()['url']
    print(url)

    # 将这个图片从内存中打开，然后就可以用Image的方法进行操作了
    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype"
    options["max_face_num"] = 5
    options["face_type"] = "LIVE"
    """ 带参数调用人脸检测 """
    imageType = "URL"
    result =client_face.detect(url,imageType,options)
    print("Result:  "+ str(result))
    return str(result).replace("\'","\"")


@app.route('/recog_car',methods=['GET','POST'])
def recog_car():
    print(request.form)
    url = request.form.to_dict()['url']
    print(url)
    response = requests.get(url) # 将这个图片保存在内存
    # 将这个图片从内存中打开，然后就可以用Image的方法进行操作了
    """ 如果有可选参数 """
    options = {}
    options["top_num"] = 20
    """ 带参数调用车辆识别 """
    result =client.carDetect(BytesIO(response.content).read(), options)
    print(result)
    return str(result).replace("\'","\"")

@app.route('/app2',methods=['GET','POST'])
def app2():
    print(request.form)
    if request.method == 'POST':  
        # POST:
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.form.to_dict().get("xxx","")获得
        # ----------------------------------------------------
        # GET:
        # request.args获得所有get参数放在一个类似dict类中,to_dict()是字典化
        # 单个参数可以通过request.args.to_dict().get('xxx',"")获得
        global cookie_data
        headers={
        'Connection': 'keep-alive',
        'Content-Type':'application/json',
        'Cookie': cookie_data,
        }
        print("Headers"+str(headers))
        print(request.form.to_dict())
        data= str(request.form.to_dict()).replace("\'","\"")
        data2={"url":"http://www.baihecard.com:8860/?code=Ziv36RTE7ebWBRs159CDt6QgtfcxXjALdpiPV68eCfo#/","usercode":"Ziv36RTE7ebWBRs159CDt6QgtfcxXjALdpiPV68eCfo","agentId":"1000003"}
        print (data)
        data2 = str(data2).replace("\'","\"")
        print("Data2 :"+data2)
        auth = requests.post(url = 'http://www.baihecard.com:8870/wxApi/user/check',data=data2,headers= headers)
        d = requests.post(url = 'http://www.baihecard.com:8870/wxPay/reqCardNo',data=data,headers= headers)
        if d.text == "PARAM ERROR":
            d = requests.post(url = 'http://www.baihecard.com:8870/wxApi/wxPay/tradeTest',data=data,headers= headers)
        print(auth.text)
        print(d.text)
        datax = request.form
        content = str(d.text) 
        resp = Response_headers(content)  
        return resp  
    else:  
        content = json.dumps({"error_code":"1001"})  
        resp = Response_headers(content)  
        return resp 


@app.route('/wp-json/wp/v2/<posts>',methods=['GET','POST'])
def wp2(posts):
    url = "blog.echo.cool/wp-json/wp/v2/"+posts
    print(request.args)
    request_data = "?"
    for i in request.args:
        print(i)
        print(request.args[i])
        request_data = request_data+i+"="+request.args[i]+"&"
    print(url+request_data)
    url = "http://"+url+request_data
    res = requests.get(url)
    #print(res.text)
    return res.text
#https://w1109790800.leanapp.cn/wp-json/wp/v2/pages/14070
@app.route('/wp-json/wp/v2/pages/<id_data>',methods=['GET','POST'])
def wppages(id_data):
    url = "blog.echo.cool/wp-json/wp/v2/pages/"+id_data
    url = "http://"+url
    res = requests.get(url)
    #print(res.text)
    return res.text

@app.route('/wp-json/wp/v2/posts/<id_data>',methods=['GET','POST'])
def wp3(id_data):
    url = "blog.echo.cool/wp-json/wp/v2/posts/"+id_data
    url = "http://"+url
    res = requests.get(url)
    #print(res.text)
    return res.text

@app.route('/wp-json/watch-life-net/v1/post/swipe',methods=['GET','POST'])
def wp4():
    url = "blog.echo.cool/wp-json/watch-life-net/v1/post/swipe"
    url = "http://"+url
    res = requests.get(url)
   # print(res.text)
    return res.text
#/wp-json/watch-life-net/v1/weixin/qrcodeimg /wp-json/watch-life-net/v1/weixin/getopenid
@app.route('/wp-json/watch-life-net/v1/weixin/<func>',methods=['GET'])
def wp29(func):
    print(request.form)
    print(request.form.to_dict())
    print(request)
    url = "blog.echo.cool/wp-json/watch-life-net/v1/weixin/"+str(func)
    url = "http://"+url
    res = requests.get(url)
   # print(res.text)
    return res.text
@app.route('/wp-json/watch-life-net/v1/weixin/getopenid',methods=['POST'])
def wp28():
    print(request.form)
    data = request.form
    url = "blog.echo.cool/wp-json/watch-life-net/v1/weixin/getopenid"
    url = "http://"+url
    res = requests.post(url,json = data )
   # print(res.text)
    return res.text
#post/like
@app.route('/wp-json/watch-life-net/v1/post/<func>',methods=['POST'])
def wp391(func):
    print(request.form)
    data = request.form
    url = "blog.echo.cool/wp-json/watch-life-net/v1/post/"+str(func)
    url = "http://"+url
    res = requests.post(url,json = data )
   # print(res.text)
    return res.text
#https://w1109790800.leanapp.cn/wp-json/watch-life-net/v1/comment/add
@app.route('/wp-json/watch-life-net/v1/comment/add',methods=['POST'])
def wp39():
    print(request.form)
    data = request.form
    url = "blog.echo.cool/wp-json/watch-life-net/v1/comment/add"
    url = "http://"+url
    res = requests.post(url,json = data )
   # print(res.text)
    return res.text
#http://localhost:3000/wp-json/watch-life-net/v1/weixin/qrcodeimg
@app.route('/wp-json/watch-life-net/v1/weixin/qrcodeimg',methods=['POST'])
def wp38():
    print(request.form)
    data = request.form
    url = "blog.echo.cool/wp-json/watch-life-net/v1/weixin/qrcodeimg"
    url = "http://"+url
    res = requests.post(url,json = data )
   # print(res.text)
    return res.text
#http://localhost:3000/wp-json/watch-life-net/v1/post/addpageview/13628
@app.route('/wp-json/watch-life-net/v1/post/addpageview/<id_data>',methods=['GET','POST'])
def wp5(id_data):
    url = "blog.echo.cool/wp-json/watch-life-net/v1/post/addpageview/"+id_data
    url = "http://"+url
    res = requests.get(url)
   # print(res.text)
    return res.text
#https://w1109790800.leanapp.cn/wp-content/plugins/wp-rest-api-for-app/qrcode/qrcode-14739.png
@app.route('/wp-content/plugins/wp-rest-api-for-app/qrcode/<file>',methods=['GET','POST'])
def wp599(file):
    url = "blog.echo.cool/wp-content/plugins/wp-rest-api-for-app/qrcode/"+file
    url = "http://"+url
    response = requests.get(url) # 将这个图片保存在内存
    response = Response(response, mimetype="image/jpeg")
    # 将这个图片从内存中打开，然后就可以用Image的方法进行操作了
   # print(res.text)
   
    return response
#http://localhost:3000/wp-json/watch-life-net/v1/options/enableComment
@app.route('/wp-json/watch-life-net/v1/options/enableComment',methods=['GET','POST'])
def wp6():
    url = "blog.echo.cool/wp-json/watch-life-net/v1/options/enableComment"
    url = "http://"+url
    res = requests.get(url)
   # print(res.text)
    return res.text
#http://localhost:3000/wp-json/watch-life-net/v1/weixin/getopenid
@app.route('/wp-json/watch-life-net/v1/weixin/getopenid',methods=['GET','POST'])
def wp7():
    url = "blog.echo.cool/wp-json/watch-life-net/v1/weixin/getopenid"
    url = "http://"+url
    res = requests.get(url)
   # print(res.text)
    return res.text
#http://localhost:3000/wp-json/watch-life-net/v1/comment/getcomments?postid=14748&limit=10&page=1&order=desc
@app.route('/wp-json/watch-life-net/v1/comment/getcomments',methods=['GET','POST'])
def wp8():
    url = "blog.echo.cool/wp-json/watch-life-net/v1/comment/getcomments"
    print(request.args)
    request_data = "?"
    for i in request.args:
        print(i)
        print(request.args[i])
        request_data = request_data+i+"="+request.args[i]+"&"
    print(url+request_data)
    url = "http://"+url+request_data
    res = requests.get(url)
    #print(res.text)
    return res.text
#https://w1109790800.leanapp.cn/wp-json/watch-life-net/v1/post/hotpostthisyear
@app.route('/wp-json/watch-life-net/v1/post/<parm>',methods=['GET','POST'])
def wp17(parm):
    url = "blog.echo.cool/wp-json/watch-life-net/v1/post/"+parm
    url = "http://"+url
    res = requests.get(url)
   # print(res.text)
    return res.text

@app.route('/robots.txt')
@app.route('/favicon.svg')
@app.route('/favicon.ico')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


@app.route('/sentMSG',methods=['GET','POST'])
def sentMSG():
    one_data={
                "TransCode":"030112",
                "OpenId":"123456789",
                "Body":"",
            }
    remind_data = ['又一个新任务？别怕，只要坚持一切都能完成',]
    res = requests.post("https://api.hibai.cn/api/index/index",json = one_data)
    res = json.loads(res.text)['Body']

    for i in res:
        remind_data.append(i['word'])
    print(request.form.to_dict())
    formid = request.form.to_dict()['formid']
    openid = request.form.to_dict()['openid']
    if(formid  != (None and "the formId is a mock one")and openid != None):
            print(formid)
            print(openid)
            keyword1={
                "value": "完成番茄时间！",
            }
            keyword2={
                "value": "今天",
            }
            keyword3={
                "value": remind_data[random.randint(0,len(remind_data)-1)],
            }
            data2={
                "keyword1":keyword1,
                "keyword2":keyword2,
                "keyword3":keyword3,
            }

            data = {
                "touser": openid,
                "template_id": "jU-T8cBTkvhQ-xCzkGP4Ef8TrfeI3qkMQ_l_ZNaP9Ik",
                "page": "pages/index/index",
                "form_id": formid,
                "data":data2,
                "emphasis_keyword": "keyword1.DATA"
            }
            headers={
                 'Connection': 'keep-alive',
                 'Content-Type':'application/json',
            }
            print(data)
            res = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx08d8f52ad361f6e8&secret=b635b95d8bda0e8dcb8cb9a989bdc4f0')
            access_token = json.loads(res.text)['access_token']
            res = requests.post("https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token="+access_token,json = data)
            print(res.text)
    return res.text




