from django.contrib import admin
from .models import *

admin.site.register([User, Delivery, Gadget, Summary])
# Register your models here.
