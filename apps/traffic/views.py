from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.traffic.models import Camera, Event
from apps.traffic.forms import CameraForm

def remote_view(request):
	cams = Camera.objects.all()
	context = {
		'cams':cams,
		'remote':True,
	}
	return render(request,'remote_view.html',context)

def transit_report(request):
	cams = Camera.objects.all()
	context = {
		'cams':cams,
		'transit':True,
	}
	return render(request,'traffic_report.html',context)

def change_date(dat):
	values = dat.split('-')
	str_date = "{}-{}-{} {}:{}".format(values[-1],values[0],values[1],'00','00')
	return str_date

def event_report(request,id_camera, date_in, date_out):
	date_in = change_date(date_in)
	date_out = change_date(date_out)
	cam = Camera.objects.get(id=id_camera)
	flag = False
	events = None
	try:
		events = Event.objects.filter(camera=cam).filter(date__gte=date_in,date__lte=date_out)
	except:
		flag = True
	context = {
		'date_in':date_in[0:10],
		'date_out':date_out[0:10],
		'cam':cam,
		'events':events,
		'transit':True,
		'flag':flag,
	}
	return render(request,'event_report.html',context)

def get_attr(attrs):
	attrs = list(attrs)
	flags = {
		'date':False,
		'hour':False,
		'cars':False,
		'status':False,
		'duration':False,
		'changes':False,
	}
	if attrs[0] == '1':
		flags['date'] = True
	if attrs[1] == '1':
		flags['hour'] = True
	if attrs[2] == '1':
		flags['cars'] = True
	if attrs[3] == '1':
		flags['status'] = True
	if attrs[4] == '1':
		flags['duration'] = True
	if attrs[5] == '1':
		flags['changes'] = True

	return flags


def event_print(request,id_camera, date_in, date_out, atribs):
	flags = get_attr(atribs)	
	cam = Camera.objects.get(id=id_camera)
	flag = False
	events = None
	try:
		events = Event.objects.filter(camera=cam).filter(date__gte=date_in,date__lte=date_out)
	except:
		flag = True
	context = {
		'date_in':date_in[0:10],
		'date_out':date_out[0:10],
		'cam':cam,
		'events':events,
		'transit':True,
		'flag':flag,
		'flags':flags,
	}
	return render(request,'event_report_print.html',context)

class CameraFormView(CreateView):
	model = Camera
	form_class = CameraForm
	template_name = 'cams_form.html'
	success_url = '/remote_view/'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['remote'] = True
		return context
		
class CameraUpdateView(UpdateView):
	model = Camera
	form_class = CameraForm
	template_name = 'edit_cam.html'
	success_url = '/remote_view/'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['remote'] = True
		return context

class CameraDeleteView(DeleteView):
	model = Camera
	template_name = 'cams_delete.html'
	success_url = reverse_lazy('remote_view')

	def post(self, request, *args, **kwargs):
		if "cancel" in request.POST:
			url = self.get_success_url()
			return HttpResponseRedirect(url)
		else:
			return super(CameraDeleteView, self).post(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['remote'] = True
		return context