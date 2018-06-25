from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/p10_2.html', {})
