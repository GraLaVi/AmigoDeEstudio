from django.contrib import admin
from .models import Room
from .models import Message
from .models import Topic

# Register your models here.

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)