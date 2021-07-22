from django.urls import path, include
from rest_framework import routers
from subscriptions.views.subscription_views import subscription_list, send_now, delete_subscription, add_subscription

urlpatterns = [
    path('', subscription_list),
    path('add', add_subscription, name="add_subscription"),
    path('sendnow/<int:subscription_id>', send_now, name="send_now"),
    path('delete/<int:subscription_id>', delete_subscription, name="delete_subscription"),
]