from django.http import HttpResponse
from django.shortcuts import render

a = "<h1>Hello Word!1</h1>"
test = "<h1>Hello Word!2</h1>"
def first_page(request):
    return render(request, './index.html', {
        'a':a,
        'test':test,
    })

