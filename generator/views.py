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
    lowercase_letters_for_password = "abcdefghijklmnopqrstuvwxyz"
    # we will get length
    length = 12
    # initialize our random password to pass to password.html
    random_password = ""
    # loop through the letters length times
    for number in range(length):
        # add a random choice to the password
        random_password += random.choice(lowercase_letters_for_password)
    # context: dictionary{} a key: value pair
    # key: 'password' is like id. On the rendered page password.html
    # value: random_password is passed to the rendered page
    return render(request, 'generator/password.html', {'password': random_password})


def work(request):
    return HttpResponse("Josh your working tomorrow")
