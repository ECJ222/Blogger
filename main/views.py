from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import features
from .models import Info
# Create your views here.
def blog(request):
	t=features.objects.all()
	context={}
	if request.method=='POST':
		if 'search' in request.POST:
			search=request.POST['info']
			context={'search':search}
	
			
	
	return render(request,'home.html',context)

def about(request):
	return render(request,'about.html')
def contact(request):
	if request.method=='POST':
		email=request.POST['email']
		message=request.POST['message']
		subject=request.POST['subject']
		MyEmail='enochchejieh@gmail.com'
		send_mail(subject,message,email,['enochchejieh@gmail.com'],fail_silently=False)
		messages.success(request,'Message sent!')

	return render(request,'contact.html')

def logoutt(request):
	info=Info.objects.all()
	if request.method=="POST":
		if 'posted' in request.POST:
			title=request.POST['title']
			#due_date=str(request.POST['due_date'])
			content=request.POST['content']
			container=Info.objects.create(title=title, content=content)
			container.save()
			
			
	return render(request,'home.html', {'info':info})
