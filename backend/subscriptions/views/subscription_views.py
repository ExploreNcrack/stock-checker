from django.http import HttpResponseNotFound, HttpResponseBadRequest
from subscriptions.tasks import pull_stock_data, send_now_stock_subscription_to_specific_email
from django.shortcuts import render, redirect
from subscriptions.models import *
from subscriptions.forms import *
from django.contrib import messages

def send_now(request, subscription_id):
    if not Subscription.objects.filter(id=subscription_id).exists():
        return HttpResponseNotFound("The subscription id is not found")
    send_now_stock_subscription_to_specific_email.delay(subscription_id)
    messages.success(request, 'Email sent')
    return redirect('/')

def subscription_list(request):
    context = {}
    subscriptions = Subscription.objects.all()
    stock_ticker_data = pull_stock_data(subscriptions)
    context["subscriptions"] = subscriptions
    context["stock_ticker_data"] = stock_ticker_data

    return render(request, 'subscription_list.html', context)

def add_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Add subscription successful')
            return redirect('/')
    else:
        form = SubscriptionForm()
    return render(request, 'add_subscription.html', { 'form' : form })

def delete_subscription(request, subscription_id):
    if request.method == 'POST': 
        subscription = Subscription.objects.filter(id=subscription_id)
        if not subscription.exists():
            return HttpResponseNotFound("The subscription id is not found")
        subscription.delete()
        messages.success(request, 'delete subscription successful')
    return redirect('/')
