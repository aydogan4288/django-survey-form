from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request, 'myapp/index.html')

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST['name'])
        print(request.POST['location'])
        print(request.POST['lang'])
        print(request.POST['comment'])
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['lang']
        request.session['comment'] = request.POST['comment']
        print("*"*50)
        return redirect('/result')
    else:
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')


def result(request):
    # return HttpResponse('Result')
    return render(request, 'myapp/result.html')

