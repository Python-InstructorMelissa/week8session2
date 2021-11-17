from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Note)
admin.site.register(Task)
admin.site.register(Document)
