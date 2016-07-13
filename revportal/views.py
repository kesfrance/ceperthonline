from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from revportal.models import Post 
from revportal.forms import PostForm 
import sys

# helper function
def encode_url(url):
    return url.replace(' ', '_')



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
    
    
# Create your views here.
def index(request):
    latest_posts = Post.objects.all().order_by('-created_at') 
    popular_posts = Post.objects.all().order_by('-views')[:5]
    
    t = loader.get_template('revportal/index.html')
    
    cont_dict = {'latest_posts': latest_posts, 
                 'popular_posts': popular_posts,
                }
                
    c = Context(cont_dict)
    return HttpResponse(t.render(c))
    

def post(request, slug):
    single_post = get_object_or_404(Post, 
            slug = slug)
    single_post.views += 1
    single_post.save()
    
    t = loader.get_template('revportal/post.html')
    c = Context({'single_post': single_post, }) 
    return HttpResponse(t.render(c))