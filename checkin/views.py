from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re

def home(request):
  return HttpResponse("Hello, Django!")

def greet(request, name):
  return render(
    request,
    'checkin/greet.html',
    {
      'name': name,
      'date': datetime.now()
    }  
  )

# def greet(request, name):
#   now = datetime.now()
#   formatted_now = now.strftime("%A, %d %B, %Y at %X")

#   match_obj = re.match("[a-zA-Z]+", name)

#   if match_obj:
#     clean_name = match_obj.group(0)
#   else:
#     clean_name = "Friend"

#   content = "Greetings, " + clean_name + "! It's " + formatted_now
#   return HttpResponse(content)

print("Shortcut: http://127.0.0.1:8000/greet/Joel")
