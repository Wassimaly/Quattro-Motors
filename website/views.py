import django

from django.conf import settings








from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		
		message_email = "Hello Flavio, \n" + "You have received a contact us message from: " + name + "\n Message: \n" + message + "\n To contact them back, here is their email: " + email 
		#send an email
		send_mail(
			subject,
			 message_email,
			  settings.EMAIL_HOST_USER,
			   ['info@quattro-kc.com'],
			    fail_silently=False)

		confirmationmsg= "Hello " + name + ',\n\nYou are receiving this email to confirm your contact us message was sent successfully. We will respond to you shortly via email.\n\nThank you for choosing us for all your automotive needs!'
		send_mail(
			subject, confirmationmsg, settings.EMAIL_HOST_USER, [email], fail_silently=False)
			



		return render(request, 'contact.html', {'name': name})
	
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def project(request):
	return render(request, 'project.html', {})

def services(request):
	return render(request, 'services.html', {})

def index(request):
	return render(request, 'index.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_number = request.POST['your-number']
		date = request.POST['date']
		time = request.POST['time']
		your_message = request.POST['your-message']
		service = request.POST['service']

		appointment = "Hello Flavio, \nYou have an appointment that needs your confirmation. Here is the appointment information: \n" "Name: "+ your_name + "\nNumber: " + your_number + "\nDate: " + date + "\nTime: " + time + "\nService: " + service + "\nMessage: " + your_message

		send_mail(
			'Appointment Request', #subject
			appointment, #message
			settings.EMAIL_HOST_USER, #from email
			['info@quattro-kc.com'], #To Email
			fail_silently=False)
			


		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_number': your_number,
			'date': date,
			'time': time,
			'your_message': your_message,
			'service': service
			})
	
	else:
		return render(request, 'index.html', {})