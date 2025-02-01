# from django.contrib import admin
# from .models import FAQ

# @admin.register(FAQ)
# class FAQAdmin(admin.ModelAdmin):
#     list_display = ('question', 'created_at')

from django.contrib import admin
from .models import FAQ

admin.site.register(FAQ)
