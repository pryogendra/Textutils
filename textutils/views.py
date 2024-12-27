from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse('''<h1>Hello Students</h1>''')
    data = {'name': 'Yogi', 'location': 'mumbai'}
    return render(request, "index.html", data)


def analyze(request):
    t1 = request.POST.get('t1')
    t2 = request.POST.get('t2')
    t3 = request.POST.get('t3')
    mobile = request.POST.get('t4')
    chk = request.POST.get('check')
    count = 0
    if chk == "charcount":
        for i in t1:
            if i != " ":
                count += 1
    if chk == 'upper':
        name = t1.upper()
        email = t2.upper()
        location = t3.upper()
    else:
        name = t1.lower()
        email = t2.lower()
        location = t3.lower()
    data = {'name': name, 'email': email, 'location': location, 'mobile': mobile}
    return render(request, 'analyze.html', data)
