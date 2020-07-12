from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,Http404
from django.shortcuts import reverse
from blog.models import Blog,User
# Create your views here.

def index(request):
    my_obj={'insert_1':'WELCOME TO WEBLOG','insert_2':'IT ABOUT YOUR VIEWS'}
    return(render(request,'verb/login.html',context=my_obj))
def desk(request):
    username = request.session.get('user')
    blogs = Blog.objects.all()
    return render(request,'verb/index.html',context={"blogs":blogs,"insert_1":"WEBLOG","insert_2":"IT ABOUT YOUR VIEWS","user":username})
def login(request):
    if request.method=='POST':
        name =request.POST['email']
        password=request.POST['pass']
        try:
            User.objects.get(username=name,password=password)
        except Exception as ex:
            print('error')
            return HttpResponse('<script> alert("sorry")</script>')

        request.session['user'] = name
        return HttpResponseRedirect(reverse('blog:desk'))

def logout(request):
    del request.session['user']
    return HttpResponseRedirect(reverse('blog:blogindex'))

def signup(request):
        if request.method=='POST':
            name=request.POST['email']
            password=request.POST['pass']
            user = User(username=name,password=password)
            user.save()
            return HttpResponseRedirect(reverse('blog:blogindex'))



def addblog(request):
    username = request.session.get('user')
    if request.method=='POST':
        blog=request.POST['blog']
        uname= User.objects.get(username=username)
        blo=Blog(username=uname,blog=blog)
        blo.save()
        return HttpResponseRedirect(reverse('blog:desk'))
    return render(request,'verb/blogpost.html',context={'user':username})
