from django.db import models

# Create your models here.


class Device(models.Model):
    # customer = models.ForeignKey(Customer.lastName, Customer.contactNo)
    stat = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    deviceId = models.AutoField(primary_key=True, unique=True)
    deviceStatus = models.CharField(max_length=100, choices=stat, default='Inactive')
    deviceContactNo = models.CharField('Active Cell no for Device', max_length=15)
    notificationCellNo = models.CharField('Cell no for Notification', max_length=15,
                                          null=True, blank=True)
    deviceAddress1 = models.CharField('Address Line 1', max_length=200,
                                      null=True, blank=True)
    deviceAddress2 = models.CharField('Address Line 2', max_length=200,
                                      null=True, blank=True)

    def __str__(self):
        return str(self.deviceId)


class Customer(models.Model):
    firstName = models.CharField('First Name', max_length=100)
    lastName = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Email')
    contactNo = models.CharField('Contact no', max_length=15)
    address1 = models.CharField('Address Line 1', max_length=200)
    address2 = models.CharField('Address Line 2', max_length=200, null=True)
    devices = models.ManyToManyField(Device)

    def __str__(self):
        return str(self.lastName)


class ThirdPartyCompany(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')
    contactNo = models.CharField('Contact No', max_length=15)
    address1 = models.CharField('Address Line 1', max_length=200)
    address2 = models.CharField('Address Line 2', max_length=200, null=True,
                                blank=True)

    def __str__(self):
        return str(self.name)


class TankStatus(models.Model):
    stat = (
        ('Empty', 'E'),
        ('Full', 'F'),
    )
    device = models.ForeignKey(Device)
    tankStatus = models.CharField(max_length=200, choices=stat, default='Empty')

    def __str__(self):
        return str(self.tankStatus)


class ThirdPartyQueue(models.Model):
    id = models.ForeignKey(Device, primary_key=True)

    def __str__(self):
        return str(self.id.deviceContactNo)
