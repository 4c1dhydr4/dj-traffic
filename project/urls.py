from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login, logout
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.login.views import index, users_admin, users_list, users_add, users_edit, UserUpdate, UserUpdate, UserDelete
from apps.traffic.views import remote_view, transit_report, CameraFormView, CameraUpdateView, CameraDeleteView, event_report, event_print


urlpatterns = [
	url(r'^$', login, {'template_name':'login.html'}, name='login'),
	url(r'^logout/', logout, {'template_name':'logout.html'}, name='logout'),
	url(r'^index/', login_required(index), name='index'),
	url(r'^remote_view/', login_required(remote_view), name='remote_view'),
	url(r'^transit_report/', login_required(transit_report), name='transit_report'),
	# url(r'^event_report/(?P<id_camera>\d+)/', login_required(event_report), name='event_report'),
	url(r'^event_report/(?P<id_camera>\d+)/(?P<date_in>\d{2}-\d{2}-\d{4})/(?P<date_out>\d{2}-\d{2}-\d{4})', login_required(event_report), name='event_report'),
	path('event_print/<int:id_camera>/<str:date_in>/<str:date_out>/<str:atribs>/', login_required(event_print), name='event_print'),
	url(r'^users_admin/', login_required(users_admin), name='users_admin'),
	url(r'^users_list/', login_required(users_list), name='users_list'),
	url(r'^users_add/', login_required(users_add), name='users_add'),
	url(r'^users_edit/', login_required(users_edit), name='users_edit'),
	url(r'^cams_add/', login_required(CameraFormView.as_view()), name='cams_add'),
	url(r'^cams_update/(?P<pk>\d+)/', login_required(CameraUpdateView.as_view()), name='cams_update'),
	url(r'^cams_delete/(?P<pk>\d+)/', login_required(CameraDeleteView.as_view()), name='cams_delete'),
	url(r'^user_update/(?P<pk>\d+)/', login_required(UserUpdate.as_view()), name='user_update'),
	url(r'^user_delete/(?P<pk>\d+)/', login_required(UserDelete.as_view()), name='user_delete'),
]
