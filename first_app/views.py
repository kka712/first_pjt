import random
from faker import Faker
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'adaf'
    
    context = {
        'my_name' : my_name,
    }

    return render(request, 'hello.html', context)


def lunch(request):
    menu = ['김밥', '국밥', '김치찌개']

    pick = random.choice(menu)

    context = {
        'pick' : pick,
    }

    return render(request, 'lunch.html', context)


def lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)

    context = {
        'lucky_numbers' : lucky_numbers,
    }

    return render(request, 'lotto.html', context)

def profile(request, username):
    context = {
        'username': username,
    }

    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3

    context = {
        'number': number,
        'result': result,
    }

    return render(request, 'cube.html', context)

def articles(request):
    fake = Faker()
    fake_articles= []

    for i in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }

    return render(request, 'articles.html', context)