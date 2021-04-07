from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def creator(request):
    return render(request, 'generator/creator.html')

def password(request):

    characters = list('abcdefghlmnopwxyzlskdflzbelzebf')
    if request.GET.get('UpperCase'):
        characters.extend(list('ABCSDLKDJFLZENKAZPOIIOZUYEIUTRBXWNCWCLB'))

    if request.GET.get('Special'):
        characters.extend(list('$*/!:;,ù'))

    if request.GET.get('Numbers'):
        characters.extend(list('123456789'))

    length = int(request.GET.get('length'),12)
    thepassword =''
    for i in range(0,length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})