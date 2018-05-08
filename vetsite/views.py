

# Create your views here.
#from django.http import HttpResponse


#def client_database(request):
#    return HttpResponse("Hello, this is the PoultryVet database")


from django.shortcuts import render
#Import models from VSDK app
from vsdk.service_development.models.session import *
#Import database information
from vetsite.clients import KasaDaka_Database

#Load data via django database utility
def call_session(request):
    call_sessions = CallSession.objects.all()
    call_session_steps = CallSessionStep.objects.all()
    sql = KasaDaka_Database.query("SELECT * FROM service_development_callsession")
    return render(request, 'vetsite/call_session.html', {'call_sessions': call_sessions, 'call_session_steps': call_session_steps, 'sql': sql})

