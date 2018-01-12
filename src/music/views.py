from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db.models import Q
from .models import Album, Song , myplay
from .forms import  User_Forms

# Create your views here.
#-----------------------------------------#


# view to define the home detail page........
def home_detail(request):
    albums = Album.objects.all()
    song_results = Song.objects.all()
    query = request.GET.get("q")
    if query:
        albums = albums.filter(
            Q(Album_title__icontains=query) |
            Q(Artist__icontains=query)
            ).distinct()
        song_results = song_results.filter(
            Q(song_title__icontains=query)
            ).distinct()
        return render(request, 'home-detail.html', {
        'albums': albums,
        'songs': song_results,
        })
    else:
        return render(request, 'home-detail.html', {'albums': albums})
	
# view to define the signup page.............
def	SignUp(request):
	form = User_Forms(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				hello='Welcome'
				albums = Album.objects.all()
				return render(request, 'after-login-home.html', {'albums': albums,'hello':hello})

	context = {
	"form": form,
	}
	return render(request, 'signup.html', context)



# view to define the detail page..........
def detail(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        user = request.user
        album = get_object_or_404(Album, pk=album_id)
        return render(request, 'detail.html', {'album': album, 'user': user})



# view to define  the logout page for app.....
def logout_user(request):
    logout(request)
    form = User_Forms(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)

# view to define the login page for app....... 
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.all()
                
                return render(request, 'after-login-home.html', {'albums': albums,})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

# view to define the user after loin page to provide thr message functionality and to provide the mlay music app detail...
def after_login_home(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:    
        albums = Album.objects.all()
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
            Q(Album_title__icontains=query) |
            Q(Artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
            Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'after-login-home.html', {
            'albums': albums,
             'songs': song_results,
                    })
        return render(request, 'after-login-home.html', {'albums': albums})


# view to define the add function to add the fav song to your play list....
def add(request,song_id):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        song = get_object_or_404(Song, pk=song_id)
        my=myplay.objects.all()
        my.mysong=song.pk
        my.save()
        albums = Album.objects.all()
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
            Q(Album_title__icontains=query) |
            Q(Artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
            Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'after-login-home.html', {
            'albums': albums,
             'songs': song_results,
                    })
        return render(request, 'after-login-home.html', {'albums': albums})


        