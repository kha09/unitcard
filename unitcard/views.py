from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import default_storage
# Create your views here.
from django.core.files import File
import os
from django.views.generic import ListView


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
            vcf_file = f'{first_name.lower()}.vcf'
            vcf_name = first_name.lower()
            vcard = make_vcard(first_name, last_name, company, title, phone, email)
            # write_vcard(vcf_file, vcard)
            f = open(vcf_file, 'w')
            f.writelines([l + '\n' for l in vcard])
            f.close()
            card = Card.objects.create(
                first_name=first_name, last_name=last_name,
                company=company, title=title,
                phone=phone, email=email,

            )
            with open(vcf_file, 'rb') as existing_file:
                    my_file = File(file=existing_file, name= vcf_file)
                    card = Vcard(filecard= my_file)
                    card.save()


                # django_image_file = File(file=existing_file, name='filename.jpeg')
                # post = Post(image=django_image_file)
                # post.full_clean()
                # post.save()


                # vcard = Vcard
                # vcard.filecard.save(vcf_file, existing_file, save=False)
                # vcard.save()

            # vcf_file = f'{first_name.lower()}.vcf'
            # vcf_name = first_name.lower()
            # vcard = make_vcard(first_name, last_name, company, title, phone, email)
            # write_vcard(vcf_file, vcard)
            # f = open(vcf_file, 'w')
            # f.writelines([l + '\n' for l in vcard])
            # f.close()

            # default_storage.save(vcf_name,vcf_file)
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


def card(request):
    cards = Vcard.objects.all()
    data = {
        'cards':cards,
    }
    return render(request, 'card.html', data)