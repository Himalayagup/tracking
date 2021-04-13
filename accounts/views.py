from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from .forms import PublisherSignUpForm, ManagerSignUpForm, OwnerSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

# def register(request):
#     return render(request, 'accounts/register.html')


class publisher_register(CreateView):
    model = User
    form_class = PublisherSignUpForm
    template_name = 'accounts/publisher_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('/')


class manager_register(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'accounts/manager_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class owner_register(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'accounts/owner_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html',
                  context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


class NotAllowed(TemplateView):
    template_name = 'accounts/not_allowed.html'
