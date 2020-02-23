from django.shortcuts import render
# The dot before models means current directory or current application
from .models import Post
from django.utils import timezone

# As you can see, we created a function (def) called post_list that takes request
    #and will return the value it gets from calling another function render that will render (put together) our template
def post_list(request):
    # To take actual blog posts from the Post model we need something called QuerySet
    # we create a variable for our QuerySet: posts. Treat this as the name of our QuerySet. From now on we can refer to it by this name.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # The last parameter, {}, is a place in which we can add some things for the template to use.
    return render(request, 'blog/post_list.html', {'posts' : posts})
