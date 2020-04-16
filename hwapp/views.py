from django.shortcuts import render
from django.shortcuts import HttpResponse
import pymysql

# Create your views here.
def index(request):
#    return HttpResponse("Hello Django World!")
    return render(request,"index.html")

def accounts(request):
    conn = pymysql.connect(host='127.0.0.1',port=3306,db='lhzhujian_db',user='root',password='123456')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from t_account')
    accounts = cursor.fetchall()

    return render(request, "account.html", {"accounts":accounts})

def login(request):
    return render(request,"login.html")

def do_login(request):
    username = ""
    password = ""
    if request.method =="POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)

    print(username,password)

    conn = pymysql.connect(host='127.0.0.1',port=3306,db="lhzhujian_db",user='root',password='123456')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from t_account where id = %s and account_name = %s',(username,password))
    if cursor.rowcount>0:
        return render(request,"success.html",{"username":username})
    else:
        return render(request,"failure.html",{"username":username})












