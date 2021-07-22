from celery import shared_task
from django.core import mail
from django.conf import settings
from subscriptions.models import *
import yfinance as yf

def format_message_body(stocks_info):
    message = ""
    for stock_info in stocks_info:
        for stock_ticker, current_price in stock_info.items():
            message += f'{stock_ticker} : ${current_price}\n'
    return message

def get_notification_email(subscriptions):
    email_message_objects = []
    for to_email, stock_tickers_info in subscriptions.items():
        message_body = format_message_body(stock_tickers_info)
        email_message = mail.EmailMessage("stock ticker update", message_body, settings.EMAIL_HOST_USER, [to_email])
        email_message_objects.append(email_message)
    return email_message_objects

def send_stock_subscription_emails(all_subscriptions, stock_ticker_data):
    subscriptions = {}
    for subscription in all_subscriptions:
        if subscription.email not in subscriptions:
            subscriptions[subscription.email] = []
        subscriptions[subscription.email].append({ subscription.stock_ticker: stock_ticker_data[subscription.stock_ticker] })
    
    connection = mail.get_connection()   # Use default email connection
    messages = get_notification_email(subscriptions)
    connection.send_messages(messages)

def pull_stock_data(subscriptions):
    stock_ticker_data = {}
    distinct_stock_tickers_from_db = subscriptions.values("stock_ticker").distinct()
    stock_tickers = [subscription["stock_ticker"] for subscription in distinct_stock_tickers_from_db]
    tickers = " ".join(stock_tickers)
    tk = yf.Tickers(tickers)
    for stock_ticker in tk.tickers:
        stock_ticker_data[stock_ticker] = round(tk.tickers[stock_ticker].info["currentPrice"], 2)
    return stock_ticker_data

@shared_task
def pull_stock_data_and_send_stock_subscription_emails_periodically():
    subscriptions = Subscription.objects.all()
    stock_ticker_data = pull_stock_data(subscriptions)
    send_stock_subscription_emails(subscriptions, stock_ticker_data)

@shared_task
def send_now_stock_subscription_to_specific_email(id):
    subscriptions = Subscription.objects.filter(id=id)
    stock_ticker_data = pull_stock_data(subscriptions)
    send_stock_subscription_emails(subscriptions, stock_ticker_data)
