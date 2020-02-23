from django.shortcuts import render

# Create your views here.

# As you can see, we created a function (def) called post_list that takes request
    #and will return the value it gets from calling another function render that will render (put together) our template
def post_list(request):
    return render(request, 'blog/post_list.html', {})
