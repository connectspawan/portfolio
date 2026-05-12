from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from portfolio import settings
from .models import Milestone, Profile, Project, Contact, Skill


def home(request):

    profile = Profile.objects.first()

    featured_projects = Project.objects.all().order_by('order')

    return render(
        request,
        'index.html',
        {
            'profile': profile,
            'featured_projects': featured_projects
        }
    )

def about(request):

    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by('order')
    milestones = Milestone.objects.all().order_by('-order')
    return render(
        request,
        'about.html',
        {
            'profile': profile,
            'skills': skills,
            'milestones': milestones
        }
    )

def projects(request):

    projects = Project.objects.all().order_by('-order')

    return render(request,
                  'projects.html',
                  {'projects': projects})

def contact(request):

    profile = Profile.objects.last()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
#         send_mail(
#             subject=f'Portfolio Contact: {subject}',

#             message=f'''
# New Portfolio Contact Form Submission

# Name: {name}
# Email: {email}
# Message:
# {message}
# ''',
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=['connectspawan@gmail.com'],
#             fail_silently=False,
#         )
        messages.success(request, 'Your message has been sent successfully to Pawan!')

        return redirect('/contact/')

    return render(
        request,
        'contact.html',
        {
            'profile': profile
        }
    )