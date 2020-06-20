from django.shortcuts import render, HttpResponse
from .models import contact

# Create your views here.
def index(request):
	return render(request, 'index.html')
	#return HttpResponse('this is first page')

def about(request):
	return HttpResponse('this is about page')



def get_value(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		sub=request.POST.get('subject')
		text=request.POST.get('message')
		use=contact()
		use.name=name
		use.email=email
		use.subject=sub
		use.message=text
		use.save()
	return HttpResponse('Thank You for contacting!!')