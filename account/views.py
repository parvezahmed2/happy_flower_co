from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import RegistrationForm, UpdateForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from rest_framework.authtoken.models import Token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
# Create your views here.




class UserRegistrationView(FormView):
    template_name = 'account/user_registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = form.save()
        self.send_activation_email(user)
        return super().form_valid(form)

    def send_activation_email(self, user):
        current_site = get_current_site(self.request)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        confirm_link = self.request.build_absolute_uri(reverse_lazy('activate', kwargs={'uid64': uid, 'token': token}))
        email_subject = 'Activate Your Flower Sales Account'
        email_body = render_to_string('account/confirm_email.html', {'confirm_link': confirm_link})
        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, "text/html")
        email.send()
    


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoseNotExist):
        user = None
    
    if user is not  None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    


class UserLoginView(LoginView):
    template_name = 'account/login.html'
     
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    

    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information  incorect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context





class UserLgoutView(LoginRequiredMixin, LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('homepage')




class UserUpdateView(View):
    template_name = 'account/profile.html'

    def get(self, request):
        form = UpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return UpdateForm('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})


def about(request):
    return render(request, 'account/about.html')