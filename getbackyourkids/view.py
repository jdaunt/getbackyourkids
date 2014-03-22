from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from getbackyourkids.models import Contacts,Comments, Counters

def gbyk(request):                      
	dbupdate = Counters.objects.get(id=1)
	dbupdate.PageHitCount = dbupdate.PageHitCount + 1
	dbupdate.save()
	return render(request, 'gbyk.html') 
	
def gbykbonus(request):                      
	contact_name = ""
	contact_email = ""
	errorflag = "N"
	error1 = ""
	error2 = ""
	if request.method == 'POST':
		if not request.POST.get('name', ''):
			errorflag = "Y"
			error1 = " *required"
		else:
			contact_name = request.POST['name']
		#end if	
		if not request.POST.get('email', ''):
			errorflag = "Y"
			error2 = " *required"
		elif request.POST.get('email') and '@' not in request.POST['email']:
			errorflag = "Y"
			error2 = " *required"
		else:
			contact_email = request.POST['email']
		#end if
		if errorflag == "Y":
			return render(request, 'gbyk.html', {'error1': error1,'error2': error2,'contact_name': contact_name, 'contact_email': contact_email})
		else:
			dbupdate = Contacts(Name=contact_name, Email=contact_email)
			dbupdate.save()
			dbupdate = Counters.objects.get(id=1)
			dbupdate.Page1Submit = dbupdate.Page1Submit + 1
			dbupdate.save()
			return render(request, 'gbykbonus.html',{'contact_name': contact_name, 'contact_email': contact_email}) 	
		#end if
	else:
		return render(request, 'gbyk.html')
	#end if	

def gbykcomments(request):                      
	contact_name = ""
	contact_email = ""
	contact_comments = ""
	errorflag = "N"
	error1 = ""
	error2 = ""
	error3 = ""
	
	if request.method == 'POST':
		if not request.POST.get('name', ''):
			errorflag = "Y"
			error1 = " *required"
		else:
			contact_name = request.POST['name']
		#end if	
		if not request.POST.get('email', ''):
			errorflag = "Y"
			error2 = " *required"
		elif request.POST.get('email') and '@' not in request.POST['email']:
			errorflag = "Y"
			error2 = " *required"
		else:
			contact_email = request.POST['email']
		#end if
		if not request.POST.get('message', ''):
			errorflag = "Y"
			error3 = " *required"
		else:
			contact_comments = request.POST['message']
		#end if	
		
		if errorflag == "Y":
			return render(request, 'gbykbonus.html', {'error1': error1,'error2': error2,'error3': error3,'contact_name': contact_name, 'contact_email': contact_email,'contact_comments': contact_comments})
		else:
			dbupdate = Counters.objects.get(id=1)
			dbupdate.Page2Submit = dbupdate.Page2Submit + 1
			dbupdate.save()
			if len(contact_comments) > 0:
				contact_comment = "Thank you for your feedback!"
				dbupdate = Comments(Name=contact_name, Email=contact_email, Comments=contact_comments)
				dbupdate.save()
			else:
				contact_comment = "Hope you enjoyed,"	
			#end if	
			return render(request, 'gbykcomments.html',{'contact_comment': contact_comment}) 
		#end if
	else:
		return render(request, 'gbyk.html')
	#end if	
		
