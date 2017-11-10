from django.shortcuts import render
from django.http import HttpResponse

# 从传来的request中提取参数
def index(request, v1, v2):
    # 构造上下文
    context = {'v1': v1, 'v2': v2}
    return render(request, 'Book/index.html', context)
