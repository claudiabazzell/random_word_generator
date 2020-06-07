from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
  return redirect('/random_word_route')

def random_word_route(request):
  word = get_random_string(length=14)
  if 'attempt' in request.session:
    print('nth pass')
    request.session['attempt'] = request.session['attempt'] + 1
    request.session['word'] = word
  else:
    print('first pass')
    request.session['attempt'] = 0
  return render(request, 'index.html')

def generate(request):
  return redirect('/')


def reset(request):
  del request.session['attempt']
  return redirect('/')


# Create your views here.
