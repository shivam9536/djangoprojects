from django.contrib import admin
from testapp.models import hydjobs,chennaijobs,punejobs,blorejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']

class blorejobsadmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','email','phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
admin.site.register(blorejobs,blorejobsadmin)
admin.site.register(chennaijobs,chennaijobsAdmin)


