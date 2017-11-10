from django.shortcuts import render
from django.http import HttpResponse

# 从传来的request中提取参数
def index(request, v1, v2):
    # 构造上下文
    context = {'v1': v1, 'v2': v2}
    return render(request, 'Book/index.html', context)

def property(requeset):
    context = {'path':requeset.path, 'method': requeset.method, 'GET':requeset.GET}

    return render(requeset, 'Book/property.html', context)

def get(request):
    return render(request, 'Book/get.html')


def get1(request):
    dict = request.GET

    a = dict.get('a')
    b = dict.get('b')
    c = dict.get('c')

    context = {'a':a, 'b':b, 'c':c}
    return render(request, 'Book/get1.html', context)

def get2(request):
    dict = request.GET

    a = dict.getlist('a')
    b = dict.get('b')
    c = dict.get('c')

    context = {'a':a, 'b':b, 'c':c}
    return render(request, 'Book/get2.html', context)

# post请求的POST属性，准备表单
def post(request):
    return render(request, 'Book/post.html')


# 获取post表单中的信息，并且在网页展示
def post1(request):
    dict = request.POST
    uname = dict.get('uname')
    upassword = dict.get('password')
    sex = dict.get('sex')
    like = dict.getlist('like')

    context = {'uname':uname, 'upwd':upassword, 'sex':sex, 'like':like}
    return render(request, 'Book/post1.html', context)