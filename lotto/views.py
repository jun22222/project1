from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .forms import *
from lotto.models import GuessNumbers, Location


def post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})
            # GET으로 들어오면 화면을 보여줘라
    else:  # post
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
        lotto.generate()
        return redirect('/lotto')
            # 제출하면 자료를 POST 방식으로 처리해라

def index(request):
    lottos = GuessNumbers.objects.all()
    location = Location.objects.get(id = 1)
    return render(request, 'lotto/lotto.html', {'lottos': lottos, 'location': location})