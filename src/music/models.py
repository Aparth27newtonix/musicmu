from django.db import models
from django.contrib.auth.models import  Permission,User

# Create your models here.
class  Album(models.Model):
	Artist=models.CharField(max_length=250)
	Album_title=models.CharField(max_length=500)
	Genre=models.CharField(max_length=50)
	Album_logo=models.FileField()

	def __str__(self):
		return self.Album_title+self.Artist


class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	song_title=models.CharField(max_length=500)
	audio_file=models.FileField(default='')

	def __str__(self):
		return self.song_title

 # Models for User play_list.


class myplay(models.Model):
	user = models.ForeignKey(User, default=1)
	mysong=models.ForeignKey(Song,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.mysong.pk
		

		

