from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('addpost/', views.AddPostView.as_view(), name='addpos'),
    path('order_history/', views.OrderHistoryView.as_view(), name='order_history'),
    path('place_order/<int:flower_id>/', views.PlaceOrderView.as_view(), name='place_order'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)