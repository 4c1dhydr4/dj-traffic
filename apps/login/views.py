from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from apps.login.forms import SignUpForm

def users_add(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users_list')
    else:
        form = SignUpForm()
    return render(request, 'user_add.html', {'form': form,'usersapp':True,})
# Create your views here.
def index(request):
	return render(request,'index.html')

def users_admin(request):
	context = {
		'usersapp':True,
	}
	return render(request,'user_admin.html',context)

def users_list(request):
	users = User.objects.all()
	context = {
		'users':users,
		'usersapp':True,
	}
	return render(request,'user_list.html',context)

def users_edit(request):
	users = User.objects.all()
	context = {
		'users':users,
		'usersapp':True,
	}
	return render(request,'user_edit.html',context)


class UserUpdate(UpdateView):
	model = User
	form_class = SignUpForm
	template_name = 'edit_user.html'
	success_url = '/users_list/'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['usersapp'] = True
		return context


class UserDelete(DeleteView):
	model = User
	template_name = 'user_delete.html'
	success_url = reverse_lazy('users_edit')

	def post(self, request, *args, **kwargs):
		if "cancel" in request.POST:
			url = self.get_success_url()
			return HttpResponseRedirect(url)
		else:
			return super(UserDelete, self).post(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['usersapp'] = True
		return context