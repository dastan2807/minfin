from django.contrib import admin
from . import models


admin.site.register(models.Person)
admin.site.register(models.Name_job)
admin.site.register(models.MainPersonUser)
admin.site.register(models.Name_otdel)

