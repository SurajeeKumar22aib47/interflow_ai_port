from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views import View
from django.conf import settings

class ContactFormView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'Message from {name}'
        message_body = f'You have received a new message from {name} ({email}):\n\n{message}'

        try:
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,  # Use your configured email address
                [settings.EMAIL_HOST_USER],  # To email (your email)
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

        return HttpResponse('Thank you for your message. We will get back to you soon.')
