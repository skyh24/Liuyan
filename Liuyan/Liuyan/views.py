from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import HttpResponse
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
PORT = 3306

def comment(request):
    db = MySQLdb.connect(user='root', db='liuyan', passwd='891010', host='localhost')
    cur = db.cursor()
    cur.execute('SELECT * FROM tb_liuyan')
    rows = cur.fetchall()
    cur.close()
    db.close()
    return render_to_response('index.html')
    #return HttpResponse(str(rows))


