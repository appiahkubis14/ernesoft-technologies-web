from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about-us.html')

def team(request):
    return render(request, 'core/team.html')

def team_details(request):
    return render(request, 'core/team-details.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')


def project(request):
    return render(request, 'core/project.html')


def project_details(request):
    return render(request, 'core/project-details.html')


def pricing(request):
    return render(request, 'core/pricing.html')


def faq(request):
    return render(request, 'core/faq.html')

def contact(request):
    return render(request, 'core/contact.html')

def service(request):
    return render(request, 'core/service.html')

def service_details(request):
    return render(request, 'core/service-details.html')

def blog_grid(request):
    return render(request, 'core/blog-grid.html')

def blog_2column(request):
    return render(request, 'core/blog-2column.html')

def blog_details(request):
    return render(request, 'core/blog-details.html')



def pro1(request):
    return render(request, 'core/projects/pro1.html')

def pro2(request):
    return render(request, 'core/projects/pro2.html')

def pro3(request):
    return render(request, 'core/projects/pro3.html')

def pro4(request):
    return render(request, 'core/projects/pro4.html')

def pro5(request):
    return render(request, 'core/projects/pro5.html')

def pro6(request):
    return render(request, 'core/projects/pro6.html')

def pro7(request):
    return render(request, 'core/projects/pro7.html')

def pro8(request):
    return render(request, 'core/projects/pro8.html')



def it_service(request):
    return render(request, 'core/services/it.html')

def geo_service(request):
    return render(request, 'core/services/geo.html')

def web_service(request):
    return render(request, 'core/services/web.html')

def mobile_service(request):
    return render(request, 'core/services/mobile.html')