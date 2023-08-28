from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    # generate the random password
    # views is where data is passed to the page

    # the lowercase letters we will use
    chars_for_password = list("abcdefghijklmnopqrstuvwxyz")
    # check for uppercase
    if request.GET.get('uppercase'):
        chars_for_password.extend(list(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # check for numbers
    if request.GET.get('numbers'):
        chars_for_password.extend(list('1234567890'))

    # check for special characters
    if request.GET.get('specialchars'):
        chars_for_password.extend(list('!@#$%^&*()_+=/\|?><'))

    # we will get length. length is an str. get request return str. cast to int
    length = int(request.GET.get('length', 12))  # 12 is a default if no
    # selection
    # initialize our random password to pass to password.html
    random_password = ""
    # loop through the letters length times.
    for number in range(length):
        # add a random choice to the password
        random_password += random.choice(chars_for_password)
    # context: dictionary{} a key: value pair
    # key: 'password' is like id. On the rendered page password.html
    # value: random_password is passed to the rendered page
    return render(request, 'generator/password.html',
                  {'password': random_password})


def work(request):
    return HttpResponse("Josh your working tomorrow")


def about(request):
    return render(request, 'generator/about.html')
