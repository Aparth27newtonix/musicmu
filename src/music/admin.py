from django.contrib import admin

from django.contrib.auth.models import User

from .models import  Album, Song ,myplay

# Register your models here.
class  AlbumAdmin(admin.ModelAdmin):
	class Meta:
		model=Album





admin.site.register(Album, AlbumAdmin)	
admin.site.register(Song)	
admin.site.register(myplay)	
 


	
		