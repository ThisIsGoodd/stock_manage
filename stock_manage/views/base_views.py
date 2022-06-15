#기본관리
from logging import exception
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

from django.db.models import Q

import requests
import json
def stock_manage(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'stock_manage/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'stock_manage/question_detail.html', context)

def search(request):
    
    try:
        ticker = request.GET['ticker']
        stock_api = requests.get("https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_be65fdc198dc4b329d155f0024a8d2b9")
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ""

    content = {'stock':stock}
    return render(request, 'common/search.html', content)

def search2(request):
    return render(request, 'common/search2.html')

def home(request):
    return render(request, 'common/home.html')