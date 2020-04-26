from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
from django.forms import inlineformset_factory
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import registerform
from .models import Info
import datetime
#18c3b35ad1msh651cef4aeaa608bp1e48d6jsn1078d72b3074

# Create your views here.
def signup(request):
	if request.method=="POST":
		form=registerform(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Account successfully Created for ' + user)
			return redirect('blog')
	else:
		form=registerform()

	
	context={'form':form}
	return render(request,'signup/signup.html',{'form':form})
	
global username
def loginpage(request):
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,'Login successfully')
			return redirect('logoutt')
		else:
			messages.warning(request,'Invalid Usename and Password')

	context={}
	return render(request,'signup/login.html',context)


def logoutt(request):
	info=Info.objects.all()
	if request.method=="POST":
		if 'posted' in request.POST:
			title=request.POST['title']
			#due_date=str(request.POST['due_date'])
			content=request.POST['content']
			container=Info.objects.create(title=title, content=content)
			container.save()
			
			
	return render(request,'signup/logout.html', {'info':info})

def delete(request,post_id):
	info=Info.objects.all()
	if request.method=="POST":
		if 'delete' in request.POST:
			info=Info.objects.get(pk=post_id)
			info.delete()
			return redirect('logoutt')

	return render(request,'signup/logout.html', {'info':info})

def about(request):
	return render(request,'signup/about.html')

def contact(request):
	if request.method=='POST':
		email=request.POST['email']
		message=request.POST['message']
		subject=request.POST['subject']
		MyEmail='enochchejieh@gmail.com'
		send_mail(subject,message,MyEmail,[email],fail_silently=False)
		messages.success(request,'Message sent!')

	return render(request,'signup/contact.html')

def loggout(request):
	logout(request)
	return redirect('blog')
