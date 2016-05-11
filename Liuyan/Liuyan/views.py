from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse
import simplejson as json
import datetime
import MySQLdb

def hello(request):
    return HttpResponse("Hello World!")

def hours_ahead(request, offset):
    try:
        off = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() #+ datetime.timedelta(hours=off)
    #assert False
    html = "<html><body>In %s hours, It will be %s </body></html>" % (offset, dt)
    return HttpResponse(html)

def template_test1(request):
    t = Template('My name is {{ name }}.')
    c = Context({name : 'Adrain'})
    return HttpResponse(t.render(c))

def template_test2(request):
    now = datetime.datetime.now()
    return render_to_response('curr_date.html', {'current_date':now})    

USER = 'root'
PASS = '891010'
DBNAME = 'liuyan'
HOST = 'localhost'
PORT = 3306

def comment(request):
    db = MySQLdb.connect(user='root', db='liuyan', passwd='891010', host='localhost')
    cur = db.cursor()
    cur.execute('SELECT count(*) from tb_liuyan')
    rows = cur.fetchall()
    cnt = rows[0]
    print cnt

    cur.execute('SELECT * FROM tb_liuyan')
    rows = cur.fetchall()
    item_list = rows
    print item_list
    
    cur.close()
    db.close()
    return render_to_response('index.html')
    #return HttpResponse(str(rows))

def cheer(request):
    dict = {}
    try:
        info = "Recv data"
        req = json.loads(request.raw_post_data)
        name = req['name']
        comment = req['comment']
        print name, comment

        info = "DB insert"
        db = MySQLdb.connect(user=USER, db=DBNAME, passwd=PASS, host=HOST)
        cur = db.cursor()
        #
        cur.close()
        db.close()
        info = "Success"
    except Error:
        print Error
    dict['message']=info
    json=simplejson.dumps(dict)
    return HttpResponse(json)
