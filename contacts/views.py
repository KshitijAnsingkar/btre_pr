from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check user has made enquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made a query on this listing')
                return redirect('/listings/'+listing_id)

        contact= Contact(listing=listing, listing_id=listing_id, name=name, email =email, phone=phone, message= message, user_id=user_id)
        contact.save()
        messages.success(request, 'Your request has been submitted. A realtor will get back to you shortly')
        return redirect('/listings/'+listing_id)


