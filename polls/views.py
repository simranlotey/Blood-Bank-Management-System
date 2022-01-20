from django.shortcuts import render
from .forms import DonorRegistration, Contact, Search
from .models import donor_Registration, sea_rch, con_tact


def home(request):
    return render(request, 'polls/base.html')


def about(request):
    return render(request, 'polls/about.html')


def donor_registration(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            context = {
                'forms': forms
            }

            return render(request, 'polls/donor_list.html', context)

        print(forms.errors)

    context_form = {
        'forms': forms
    }

    return render(request, 'polls/donor_registration.html', context_form)


def search(request):
    forms = Search()
    if request.method == 'POST':
        forms = Search(request.POST)
        if forms.is_valid():
            forms.save()
            bloodgroup = forms.cleaned_data['blood_group']
            state = forms.cleaned_data['state']
            city = forms.cleaned_data['city']
            donor_filter = donor_Registration.objects.filter(blood_group=bloodgroup,
                                                             state=state,
                                                             city=city,
                                                             )
            context = {
                'donor_filter': donor_filter
            }

            return render(request, 'polls/search_list.html', context)

        print(forms.errors)

    context_form = {
        'forms': forms
    }

    return render(request, 'polls/search.html', context_form)


def search_info(request, email):
    email = email
    detail = donor_Registration.objects.get(email=email)

    context = {
        'details': detail
    }

    return render(request, 'polls/search_info.html', context)


def contact(request):
    forms = Contact()
    if request.method == 'POST':
        forms = Contact(request.POST)
        if forms.is_valid():
            forms.save()

    context = {
        'forms': forms
    }

    return render(request, 'polls/contact.html', context)