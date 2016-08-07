from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from revportal.models import Post 
from revportal.forms import PostForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import sys

# helper function
def encode_url(url):
    return url.replace(' ', '_')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def user_login(request):
    context = RequestContext(request)
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
        return render_to_response('login.html', {}, context)

def user_signup(request):
    context = RequestContext(request)
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
            
            registered = True
        
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render_to_response(
            'signup.html',
            {'user_form':user_form, 'profile_form':profile_form,
             'registered' : registered
             }, context
        )
            
            

def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #print >>sys.stderr, form.cleaned_data
            #post_url = form.cleaned_data.get('title').replace(" ", "_")
            form.save(commit=True)
            return redirect(index)
        else:
            print form.errors
    else:
        form = PostForm()
    return render_to_response('revportal/add_post.html', {'form': form}, context)
    
    
@login_required
def index(request):
    latest_posts = Post.objects.all().order_by('-created_at') 
    popular_posts = Post.objects.all().order_by('-views')[:5]
    
    t = loader.get_template('revportal/index.html')
    
    cont_dict = {'latest_posts': latest_posts, 
                 'popular_posts': popular_posts,
                }
                
    c = Context(cont_dict)
    return HttpResponse(t.render(c))
    
@login_required
def post(request, slug):
    single_post = get_object_or_404(Post, 
            slug = slug)
    single_post.views += 1
    single_post.save()
    
    t = loader.get_template('revportal/post.html')
    c = Context({'single_post': single_post, }) 
    return HttpResponse(t.render(c))