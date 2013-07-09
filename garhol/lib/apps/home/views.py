from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    context = {}
   
    context['homecontent'] = "This is content from the home application"
    
    template = 'index.html'
    return render_to_response(template, context, context_instance=RequestContext(request))
    