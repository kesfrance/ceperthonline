from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from revportal.models import Post, UserProfile
from revportal.forms import PostForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import os

from ceperth.settings import MEDIA_ROOT, STATIC_ROOT, MEDIA_URL, STATIC_URL


# helper function
def encode_url(url):
    return url.replace(' ', '_')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


   

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/reviewportal/')
            else:
                return HttpResponse("Your account has been diasbled")
        else:
            print "Invalid login details: %s %s" %(username, password)
            return HttpResponse('Inavlid login details supplied.')
    else:
        req = request
        return render(request, 'login.html', {})

def user_signup(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
            
            registered = True
        
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request,
            'signup.html',
            {'user_form':user_form, 'profile_form':profile_form,
             'registered' : registered})
            

def add_newtitle(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            #print >>sys.stderr, form.cleaned_data
            #post_url = form.cleaned_data.get('title').replace(" ", "_")
            form.save(commit=True)
            return HttpResponseRedirect('/reviewportal/')
        else:
            print form.errors
    else:
        form = PostForm()
    return render(request, 'revportal/add_newtitle.html', {'form': form})
    
    
@login_required
def all_titles(request):
    latest_posts = Post.objects.all().order_by('-created_at') 
    popular_posts = Post.objects.all().order_by('-views')[:5]
    
    dic = {'latest_posts': latest_posts, 
                 'popular_posts': popular_posts,
                }
    return render(request,'revportal/alltitles.html', dic)


    
@login_required
def one_title(request, slug):
    single_post = get_object_or_404(Post, 
            slug = slug)
    single_post.views += 1
    single_post.save()
    
    profiles = UserProfile.objects.all()
    
    dic = {'single_post': single_post,
           'profiles': profiles
           }
    
    return render(request, 'revportal/singletitle.html', dic)



