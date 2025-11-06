from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('team-details/', views.team_details, name='team_details'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('project/', views.project, name='project'),
    path('project-details/', views.project_details, name='project_details'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('service-details/', views.service_details, name='service_details'),
    path('blog-grid/', views.blog_grid, name='blog_grid'),
    path('blog-2column/', views.blog_2column, name='blog_2column'),
    path('blog-details/', views.blog_details, name='blog_details'),


    path('projects/afarisense/', views.pro1, name='pro1'),
    path('projects/edur-cocoa/', views.pro2, name='pro2'),
    path('projects/amp-logistics/', views.pro3, name='pro3'),
    path('projects/human-rights/', views.pro4, name='pro4'),
    path('projects/eximbank/', views.pro5, name='pro5'),
    path('projects/kapture-gis/', views.pro6, name='pro6'),
    path('projects/hcms/', views.pro7, name='pro7'),
    path('projects/gps-tracking/', views.pro8, name='pro8'),

    path('services/it/', views.it_service, name='it_service'),
    path('services/web-development/', views.web_service, name='web_service'),
    path('services/geospatial/', views.geo_service, name='geo_service'),
    path('services/mobile-development/', views.mobile_service, name='mobile_service'),
]