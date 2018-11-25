# coding: utf-8

from datetime import datetime
from datetime import timedelta
import random
from leancloud import Object
from leancloud import ACL
from leancloud import Engine
from leancloud import LeanEngineError
from leancloud import Query
from app import app
import leancloud
import requests,json,datetime
engine = Engine(app)
global remind_data
remind_data=['这个任务还没有完成，记得去完成哦~','又一个新任务？别怕，只要坚持一切都能完成','']
@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')
    author = todo.get('author')
    if author:
        acl = ACL()
        acl.set_public_read_access(False)
        acl.set_read_access(author.id, True)
        acl.set_write_access(author.id, True)
        todo.set_acl(acl)




@engine.define
def sentMSG():
    global  remind_data
    print("Len of remind_data: "+str(len(remind_data)))
    one_data={
                "TransCode":"030112",
                "OpenId":"123456789",
                "Body":"",
            }
    cql_string1 = 'select * from Todo where sent = 0 AND done = false'
    sent_list = leancloud.Query.do_cloud_query(cql_string1).results
    res = requests.post("https://api.hibai.cn/api/index/index",json = one_data)
    res = json.loads(res.text)['Body']
    for i in res:
        remind_data.append(i['word'])
    #res = requests.get("https://api.lwl12.com/hitokoto/v1?encode=realjson")
    #print(json.loads(res.text))
    #print(sent_list)
    for i in sent_list:
        #print(i)
        formid = i.get("formid")
        openid = i.get("openid")
        content = i.get("content")
        time  = i.get("createdAt").strftime('%Y-%m-%d %H:%M:%S')
        #print(type(time))
        if(formid  != (None and "the formId is a mock one")and openid != None):
            print(formid)
            print(openid)
            one_data={
                "TransCode":"030111",
                "OpenId":"123456789",
                "Body":"",
            }
            
            keyword1={
                "value": content,
            }
            keyword2={
                "value": "未完成",
            }
            keyword3={
                "value": time,
            }
            keyword4={
                "value": remind_data[random.randint(0,len(remind_data)-1)],
            }
            data2={
                "keyword1":keyword1,
                "keyword2":keyword2,
                "keyword3":keyword3,
                "keyword4":keyword4,
            }

            data = {
                "touser": openid,
                "template_id": "FLkxzGbedW0qc3y5Wu6kfAkJ3eQz7A0cVi5bMzku_O0",
                "page": "pages/index/index",
                "form_id": formid,
                "data":data2,
                "emphasis_keyword": "keyword1.DATA",
            }
            headers={
                 'Connection': 'keep-alive',
                 'Content-Type':'application/json',
            }
           # print(data)
            res = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx08d8f52ad361f6e8&secret=b635b95d8bda0e8dcb8cb9a989bdc4f0')
            access_token = json.loads(res.text)['access_token']
            res = requests.post("https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token="+access_token,json = data)
            #print(res.text)
            
            i.set('sent', 1)
            i.set('statue_MSG',res.text)
            i.save()
    return "Done"



@engine.define
def Longtime():
    need_send_user = Object.extend('weather').query.equal_to('sent', 0).less_than('updatedAt', datetime.today() - timedelta(5)).find()
    for i in sent_list:
        print(i)
        formid = i.get("formid")
        openid = i.get("openid")
        time  = i.get("createdAt").strftime('%Y-%m-%d %H:%M:%S')
        
        print(type(time))
        if(formid  != (None and "the formId is a mock one")and openid != None):
            print(formid)
            print(openid)
            keyword1={
                "value": "很久没有打卡我的任务清单了，记得去完成哦~",
            }
            keyword2={
                "value": "未完成",
            }
            keyword3={
                "value": time,
            }
            keyword4={
                "value": "这个任务还没有完成，记得去完成哦~",
            }
            data2={
                "keyword1":keyword1,
                "keyword2":keyword2,
                "keyword3":keyword3,
                "keyword4":keyword4,
            }

            data = {
                "touser": openid,
                "template_id": "FLkxzGbedW0qc3y5Wu6kfAkJ3eQz7A0cVi5bMzku_O0",
                "page": "/pages/index/index",
                "form_id": formid,
                "data":data2,
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
            
            i.set('sent', 1)
            i.save()
    return res.text