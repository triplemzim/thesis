from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
from control.models import *


def Home(request):
    return HttpResponse('Game Over!')


def CustomerRegistration(request):
    return HttpResponse('Under construction')


def DeviceRegistration(request):
    return HttpResponse('Under construction')


def SetupDevice(request):
    if request.method == 'POST':
        contactNo = request.POST.get('contactNo', '')
        devices = Device.objects.filter(deviceContactNo=contactNo)
        device = devices[0]
        if device.deviceStatus == 'Active':
            return HttpResponse('Active')
        return HttpResponse('Inactive')


def DeviceCom(request, contactNo, msg):
    devices = Device.objects.filter(deviceContactNo=contactNo)
    device = devices[0]
    users = Customer.objects.filter(devices=device)
    user = users[0]

    print(device)
    print(user)

    if msg == 'E' and device.deviceStatus == 'Active':
        entry = ThirdPartyQueue(id=device)
        companies = ThirdPartyCompany.objects.all()
        company = companies[0]
        smsToCompany = '88' + company.contactNo
        try:
            entry.save()
            sub = 'Tank Status'
            body = 'Your water tank is currently empty. We have notified the' \
                   ' water providing company. Thank you.'
            to = user.email

            sendEmail(sub, body, to)
            sendsms(str(device.deviceAddress1), smsToCompany)

        except Exception as e:
            return HttpResponse('Failed')
    elif msg == 'F' and device.deviceStatus == 'Active':
        entry = ThirdPartyQueue.objects.get(id=device)
        try:
            entry.delete()
            sub = 'Tank Status'
            body = 'Your water tank has been filled up. Thank you.'
            to = user.email

            sendEmail(sub, body, to)
        except Exception as e:
            return HttpResponse('Failed')
    elif msg == 'A':
        device.deviceStatus = 'Active'
        try:
            device.save()
            sub = 'Device Status'
            body = 'Your device is now active. Thank you.'
            to = user.email
            sendEmail(sub, body, to)
        except Exception as e:
            return HttpResponse('Failed')
        return HttpResponse('Success')
    elif msg == 'I':
        device.deviceStatus = 'Inactive'
        try:
            device.save()
            sub = 'Device Status'
            body = 'Your device is now inactive. Thank you.'
            to = user.email
            sendEmail(sub, body, to)
        except Exception as e:
            return HttpResponse('Failed')
        return HttpResponse('Success')

    return HttpResponse('DeviceCom under construction' + str(contactNo) +
                        'msg = ' + str(msg) + str(device.deviceAddress1))


def sendemail(request):
    try:
        send_mail('', 'You Tank has been filled up. Thank you',
                  'dummylocked@gmail.com', ['8801829674014@sms.clicksend.com'],
                  fail_silently=False)
    except Exception as e:
        return HttpResponse(str(e))
    return HttpResponse('Success sending email')


def sendsms(body, number):
    # intentional spelling mistake
    to = '88' + number + '@sms.clicksendd.com'
    try:
        send_mail('', body,
                  'dummylocked@gmail.com', [to],
                  fail_silently=False)
    except Exception as e:
        return str(e)
    return 'Success' + to


def sendEmail(sub, body, to):
    try:
        send_mail(sub, body, 'dummylocked@gmail.com', [to], fail_silently=False)
    except Exception as e:
        return str(e)

    return 'Success'
