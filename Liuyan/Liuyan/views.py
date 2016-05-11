from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
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
    cnt = rows[0][0]
    print cnt

    cur.execute('SELECT * FROM tb_liuyan ORDER BY likes')
    rows = cur.fetchall()
    print rows
    item_list = []
    for row in rows:
        item = {}
        item["cid"] = row[0]
        item["name"] = row[1]
        item["comm"] = row[2]
        item["like"] = row[3]
        item_list.append(item)
    print item_list
    
    cur.close()
    db.close()
    return render_to_response('index.html', {"count": cnt, "item_list": item_list})
    #return HttpResponse(str(rows))

@csrf_exempt
def cheer(request):
    dict = {}
    try:
        info = "Recv data"
        #req = json.loads(request.raw_post_data)
        name = request.POST['name']
        comment = request.POST['comm']
        print name, comment

        info = "DB insert"
        db = MySQLdb.connect(user=USER, db=DBNAME, passwd=PASS, host=HOST)
        cur = db.cursor()
        cur.execute('insert into tb_liuyan (user, comment, likes) values (%s, %s, 1)' % (name, comment));
        db.commit()
        #
        cur.close()
        db.close()
        info = "Success"
    except Exception, e:
        print "%s" % str(e)
    dict['message']=info
    myjson=json.dumps(dict)
    return HttpResponse(myjson)

@csrf_exempt
def like(request):
    try:
        info = "Recv data"
        cid = request.POST['cid']
        db = MySQLdb.connect(user=USER, db=DBNAME, passwd=PASS, host=HOST)
        cur = db.cursor()
        info = "DB select"
        cur.execute("select likes from tb_liuyan where cid=%s" % cid);
        rows = cur.fetchall()
        likes = rows[0][0]
        likes += 1
        print "cid like", cid, likes

        info = "DB insert"
        cur.execute('update tb_liuyan likes=%s where cid=%s ' % (likes, cid));
        db.commit()
        cur.close()
        db.close()
        info = "Success"
    except Exception, e:
        print "%s" % str(e) 
    return HttpRespnse(info)
