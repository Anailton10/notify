from django.contrib import admin
from django.urls import path
from webhooks import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/webhooks/order/', views.WebHookOrderView.as_view(),name='webhook_order')
]
