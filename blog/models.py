# All lines starting with from or import are lines that add some bits from other files.
# So instead of copying and pasting the same things in every file, we can include some parts with from ... import ...
from django.conf import settings
from django.db import models
from django.utils import timezone

# class Post(models.Model): – this line defines our model (it is an object).
# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
class Post(models.Model):
    # models.ForeignKey – this is a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # def means that this is a function/method and publish is the name of the method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Methods often return something.
    # There is an example of that in the __str__ method.
    # In this scenario, when we call __str__() we will get a text (string) with a Post title
    def __str__(self):
        return self.title

# for more details - https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
