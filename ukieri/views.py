# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from mysite.ukieri.models import *
from django.template import RequestContext
from django.core.urlresolvers import reverse


def index(request):
   events = Events.objects.all()
   contact = Contact.objects.all().order_by('-id')
   participants = Participants.objects.all()
   schedule = Schedule.objects.all()
   diamond = Diamond.objects.all().order_by('-id')
   gold = Gold.objects.all().order_by('-id')
   silver = Silver.objects.all().order_by('-id')
   sponsorship = Sponsorship.objects.all()
   delegate = DelegateFees.objects.all()
   return render_to_response('ukieri/index.html', {'diamond': diamond, 'gold':gold, 'silver':silver,'events': events, 'contact': contact, 'participants': participants, 'schedule': schedule, 'sponsorship': sponsorship, 'delegate': delegate}, context_instance=RequestContext(request))

def home(request):
   events = Events.objects.all()
   contact = Contact.objects.all().order_by('-id')
   participants = Participants.objects.all()
   schedule = Schedule.objects.all()
   diamond = Diamond.objects.all().order_by('-id')
   gold = Gold.objects.all().order_by('-id')
   silver = Silver.objects.all().order_by('-id')
   sponsorship = Sponsorship.objects.all()
   delegate = DelegateFees.objects.all()
   return render_to_response('ukieri/index.html',locals())

def participants(request):
   participants = Participants.objects.all().order_by('id')
   return render_to_response('ukieri/participants.html', {'participants': participants })

def sponsorship(request):
   sponsorship = Sponsorship.objects.all().order_by('id')
   delegate = DelegateFees.objects.all()
   return render_to_response('ukieri/sponsorship.html', {'sponsorship': sponsorship, 'delegate': delegate})

def events(request):
   events = Events.objects.all().order_by('id')
   return render_to_response('ukieri/events.html', {'events': events })
def program(request):
   program = Program.objects.all().order_by('date')
   return render_to_response('ukieri/program.html', {'program': program })
def schedule(request):
   schedule = Schedule.objects.all().order_by('id')
   return render_to_response('ukieri/schedule.html', {'schedule': schedule})

def contact(request):
   contact = Contact.objects.all().order_by('-id')
   return render_to_response('ukieri/contact.html', {'contact': contact})

def audience(request):
   audience = Audience.objects.all().order_by('-id')
   delegate = DelegateFees.objects.all()
   return render_to_response('ukieri/audience.html', {'audience': audience,'delegate':delegate})

def reach(request):
    return render_to_response('ukieri/how_to_reach.html')

def sponsors(request):
   diamond = Diamond.objects.all().order_by('-id')
   gold = Gold.objects.all().order_by('-id')
   silver = Silver.objects.all().order_by('-id')
   return render_to_response('ukieri/sponsors.html', {'diamond': diamond, 'gold':gold, 'silver':silver})

def header(request):
   variables = Variables.objects.all()
   return render_to_response('ukieri/header.html', {'variables': variables})

def credits(request):
   
   return render_to_response('ukieri/credits.html' )

def travel(request):
   travel = Travel.objects.all().order_by('-id')
   return render_to_response('ukieri/travel.html', {'contact': travel})

def exhibitors(request):
   variables = Variables.objects.all()
   return render_to_response('ukieri/exhibitors.html', {'variables': variables})
