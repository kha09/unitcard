from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company = request.POST['company']
        title = request.POST['title']
        phone = request.POST['phone']
        email = request.POST['email']

        if Card.objects.filter(first_name=first_name, last_name=last_name).exists():
            return redirect('home')

        else:
            card = Card.objects.create(
                first_name=first_name, last_name=last_name,
                company=company, title=title,
                phone=phone, email=email
            )
            vcf_file = f'{first_name.lower()}.vcf'
            vcard = make_vcard(first_name, last_name, company, title, phone, email)
            write_vcard(vcf_file, vcard)

            return redirect('home')


    return render(request, 'home.html')


def make_vcard(
        first_name,
        last_name,
        company,
        title,
        phone,
        email):
    return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'REV:1',
        'END:VCARD'
    ]

def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])