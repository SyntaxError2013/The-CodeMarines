from django.http import HttpResponse


def search_constituencies(request,place):
  #search_form = loader.get_template('fillupform.html')
  try:
    return direct_to_template(request, template='fillupform.html' %place)
  except TemplateDoesNotExist:
    raise Http404()
  

def home_page(request, page){
  try:
    return direct_to_template(request, template='homepage.html' %page)
  except TemplateDoesNotExist:
    raise Http404()
