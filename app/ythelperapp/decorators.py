from django.shortcuts import redirect
from django.contrib import messages as msg
from django.utils import timezone
from .models import Ticket

import datetime
import logging

logger = logging.getLogger('youtube_helper')


def login_check(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, {'logged': True, 'username': request.user.username} , *args, **kwargs)
        else:
            return view_func(request, {'logged': False} , *args, **kwargs)
    
    return wrapper_func


def login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            msg.info(request, "You need to have account")
            return redirect('downloader_page')
        
    return wrapper_func


def not_authenticated_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            msg.info(request, "You need to log out")
            return redirect('downloader_page')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func


def rate_limit(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            user_ticket, created = Ticket.objects.get_or_create(user=request.user)

            current_time = datetime.datetime.now(datetime.timezone.utc)
            reset_time = user_ticket.last_reset_time + datetime.timedelta(hours=24) 

            if created:
                user_ticket.remaining_tickets = 3
                user_ticket.save()

            if current_time > reset_time:
                user_ticket.remaining_tickets = 3
                current_time = timezone.now().astimezone()
                user_ticket.last_reset_time = current_time.replace(hour=0, minute=0, second=0, microsecond=0)
                user_ticket.save()

            if user_ticket.remaining_tickets <= 0:
                return view_func(request, *args, **kwargs)

            user_ticket.save()
            logger.info(f"User {request.user.username} used Ticket")


        return view_func(request, *args, **kwargs)
    
    return wrapper_func
