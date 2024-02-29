from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView
from django.views import View
from .models import Flower, Order, Category
from django.core.mail import send_mail
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
# Create your views here.


class FlowerListView(ListView):
    model = Flower
    template_name = 'home.html'
    context_object_name = 'flowers'
        
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context





class PlaceOrderView(LoginRequiredMixin, View):
    def get(self, request, flower_id):
        flower = Flower.objects.get(pk=flower_id)
        return render(request, 'flower/place_order.html', {'flower': flower})

    def post(self, request, flower_id):
        flower = Flower.objects.get(pk=flower_id)
        quantity = int(request.POST.get('quantity'))
        if flower.quantity >= quantity:
            order = Order.objects.create(flower=flower, user=request.user, quantity=quantity)
            flower.quantity -= quantity
            flower.save()
            order.save()
            # Send email notification
            email_subject = 'Order Confirmation'
            email_message = render_to_string('flower/order_confirmation_email.html', {'order': order})
            email = EmailMultiAlternatives(email_subject, '', to=[request.user.email])
            email.attach_alternative(email_message, "text/html")
            email.send()
            return redirect('homepage')
        return render(request, 'flower/place_order.html', {'flower': flower})




class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'flower/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    




# post create -----------
class AddPostView(LoginRequiredMixin, CreateView):
    form_class = forms.PostForm
    template_name = 'flower/add_post.html'
    success_url = reverse_lazy('addpos')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)