from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template

# Create your views here.
def main_page(request):
  # template = get_template('main_page.html')
  variables = Context({
    'head_title': 'Django Bookmarks',
    'page_title': 'Welcome to Django Bookmarks',
    'page_body': 'Where you can store and share bookmarks!'
  })
  # output = template.render(variables)
  # return HttpResponse(output)
  return render(request, 'bookmarks/main_page.html', variables)

def user_page(request, username):
  try:
    user = User.objects.get(username=username)
  except:
    raise Http404('Requested user not found.')

  bookmarks = user.bookmark_set.all()

  template = get_template('user_page.html')
  variables = Context({
    'username': username,
    'bookmarks': bookmarks
  })
  output = template.render(variables)
  return HttpResponse(output)