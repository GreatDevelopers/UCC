from django.shortcuts import render_to_response
from mysite.student.models import *

def fulldetail(request):
	"""
	Detail Veiw of data
	"""
	fulldetail = Profile.objects.all().order_by('class_roll_no')
	return render_to_response("userprofile/profile/fulldetail.html", {"fulldetail" : fulldetail} )

def detail(request):
	"""
	Detail Veiw of data
	"""
	detail = Profile.objects.get(class_roll_no=request.GET['class_roll_no'])
	return render_to_response("userprofile/profile/detail.html", {"detail" : detail} )

def it(request):
	"""
	Detail Veiw of data
	"""
	fulldetail = Profile.objects.all().filter(branch='Information Technology')
	count =fulldetail.count() 
	return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )

def cse(request):
	"""
	Detail Veiw of data
	"""
	fulldetail = Profile.objects.all().filter(branch='Computer Science & Engineering')
	count =fulldetail.count()
	return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )

def ece(request):
	"""
	Detail Veiw of data
	"""
	
	fulldetail = Profile.objects.all().filter(branch='Electronics & Communication Engineering')
	count =fulldetail.count()
	return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )

def ce(request):
	"""
	Detail Veiw of data
	"""
	fulldetail = Profile.objects.all().filter(branch='Civil Engineering')
	count =fulldetail.count()
	return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )
	
def me(request):
	"""
	Detail Veiw of data
	"""
	fulldetail = Profile.objects.all().filter(branch='Mechanical Engineering')
	count =fulldetail.count()
	return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )
	
def pe(request):
	"""
	Detail Veiw of data
	"""
	fulldetail = Profile.objects.all().filter(branch='Production Engineering')
	count =fulldetail.count()
	return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )
def mba(request):
        """
        Detail Veiw of data
        """
        fulldetail = Profile.objects.all().filter(branch='MBA')
        count =fulldetail.count()
        return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )
               
def ee(request):
	"""
	Detail Veiw of data
	"""
	fulldetail = Profile.objects.all().filter(branch='Electrical Engineering')
	count =fulldetail.count()
	return render_to_response("userprofile/profile/it.html", {"fulldetail" : fulldetail,"count":count} )
