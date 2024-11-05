from django.shortcuts import render
def index(request):
    context = {
        'active_link': 'home'
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'active_link':'about'
    }
    return render(request, 'about.html',context)