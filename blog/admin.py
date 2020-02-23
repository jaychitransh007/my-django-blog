from django.contrib import admin
# we import (include) the Post model defined in the previous chapter
from .models import Post

# Register your models here.

# To make our model visible on the admin page, we need to register the model with admin.site.register(Post)
admin.site.register(Post)
