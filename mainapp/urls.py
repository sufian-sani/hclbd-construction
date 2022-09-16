from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('products', products, name='products'),
    path('product/<slug>/', productdetails, name='productdetails'),
    path('group/', group, name='group'),
    path('group/<slug>/', groupdetails, name='groupdetails'),
    path('boardofdirectors/', boardofdirectors, name='boardofdirectors'),
    path('boardofdirectors/<slug>/', boardofdirectorsdetails, name='boardofdirectorsdetails'),
    path('historyandmilestones/', historyandmilestones, name='historyandmilestones'),
    path('historyandmilestones/<slug>/', historyandmilestonesdetails, name='historyandmilestonesdetails'),
    path('boardmeetingsandagm/', boardmeetingsandagm, name='boardmeetingsandagm'),
    path('boardmeetingsandagm/<slug>/', boardmeetingsandagmdetails, name='boardmeetingsandagmdetails'),
    path('press-release/', news, name='news'),
    path('press-release/<slug>/', newsdetails, name='newsdetails'),
    path('corporategovernance/', corporategovernance, name='corporategovernance'),
    path('corporategovernance/<slug>/', corporategovernancedetails, name='corporategovernancedetails'),
    path('corporatesocialresponsibility/', corporatesocialresponsibility, name='corporatesocialresponsibility'),
    path('contact/', contact, name='contact'),
    path('about-us/', aboutus, name='aboutus'),
    path('client/', client, name='client'),
    path('client/<slug>/', clientdetails, name='clientdetail'),
    path('team/', team, name='team'),
    path('team/<slug>/', teamdetails, name='teamdetail'),
    path('md-message/', md_messages, name='mdmessage'),
    path('mission-vission-goal/', missionVV, name='mission-vission-goal'),
    path('supply-history/', supplyhistory, name='supply-history'),
    path('carrer/', carrer, name='carrer'),
    path('carrerdetails/<slug>/', carrerdetails, name='carrerdetails'),
    path('events/', event, name='event'),
    path('event/<slug>/', eventdetails, name='eventdetail'),
    path('notice/', notice ,name='notice'),
    path('reportstatement/', reportstatement ,name='reportstatement'),
    path('services/', service, name='service'),
    path('service/<slug>/', service_details, name='servicedetails'),
    path('blog/', blog, name='blog'),
    path('blog/<slug>/', blogdetails, name='blogdetails'),
    path('photogallery/', photogallery, name='photogallery'),
    path('videogallery/', videogallery, name='videogallery'),
]