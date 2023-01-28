from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import default_storage
# Create your views here.
from django.core.files import File
import os
from django.views.generic import ListView
import qrcode

urlcard =''
path1 = ''
def home(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company = request.POST['company']
        title = request.POST['title']
        phone = request.POST['phone']
        email = request.POST['email']
        website = request.POST['website']

        if Card.objects.filter(first_name=first_name, last_name=last_name).exists():
            return redirect('home')

        else:
            vcf_file = f'{first_name.lower()}.vcf'
            vcf_card = f'{first_name.lower()}.png'

            vcf_name = first_name.lower()
            vcard = make_vcard(first_name, last_name, company, title, phone, email, website)
            # write_vcard(vcf_file, vcard)
            f = open(vcf_file, 'w')
            f.writelines([l + '\n' for l in vcard])
            f.close()
            card = Card.objects.create(
                first_name=first_name, last_name=last_name,
                company=company, title=title,
                phone=phone, email=email,
                website=website,

            )
            with open(vcf_file, 'rb') as existing_file:
                    my_file = File(file=existing_file, name= vcf_file)
                    card = Vcard(filecard= my_file)
                    card.save()
                    urlcard = card.filecard.url
                    path1 = card.filecard.name


            input_data = urlcard

            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
            qr.add_data(input_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(vcf_card)
            with open(vcf_card, 'rb') as existing_file:
                    my_file = File(file=existing_file, name= vcf_card)
                    card = Vcard.objects.get(filecard= path1)
                    card.imgcard = my_file
                    card.save()

            return redirect('home')


    return render(request, 'home.html')


def make_vcard(
        first_name,
        last_name,
        company,
        title,
        phone,
        email,
        website):
    return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'ORG:{company}',
        f'TITLE:{title}',
        f'EMAIL;PREF;INTERNET:{email}',
        f'TEL;WORK;VOICE:{phone}',
        f'URL;WEB;WEBSITE:{website}',
        f'REV:1',
        'END:VCARD'
    ]

def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])


def card(request):
    cards = Vcard.objects.all()
    # codes = Scard.objects.all()
    data = {
        'cards':cards,
        # 'codes':codes,
    }
    return render(request, 'newcard.html', data)