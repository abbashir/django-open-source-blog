from other_pages.forms import ContactForm
from django.shortcuts import redirect, render
from .models import About, Contact
from django.contrib import messages

# Create your views here.


def about(request):
    about = About.objects.all().order_by('id').first()

    context = {
        "title": "About Page",
        "about": about,
    }
    return render(request, 'other_pages/about.html', context)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            obj = contact_form.save(commit=False)
            obj.save()
            messages.success(request, 'message sent successfully')
            return redirect('posts:home')

    contact = Contact.objects.all().order_by('id').first()

    context = {
        "title": "Contact Page",
        "contact": contact,
        "contact_form": contact_form,
    }
    return render(request, 'other_pages/contact.html', context)
