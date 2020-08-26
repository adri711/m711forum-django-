from django.contrib import admin
from . import models

admin.site.register(models.board)

admin.site.register(models.post)