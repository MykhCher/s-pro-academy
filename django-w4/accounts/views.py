from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View

class RegisterFromView(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('book_list')
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginFromView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('book_list')
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)

class LogoutFromView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('book_list'))