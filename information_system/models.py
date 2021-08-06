from django.db import models
from viewflow.models import Process
# Create your models here.

class Members(models.Model):
    AccountNumber=models.IntegerField()
    FirstName=models.CharField(max_length=20, null=True, blank=True)
    LastName = models.CharField(max_length=20, null=True, blank=True)
    Address = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField()
    Mobile=models.DecimalField(max_digits=13, decimal_places=2)
    Date_start=models.DateTimeField(auto_now=True)
    Is_active=models.BooleanField(default=False)
    Base_fund=models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = "Members"
    def __str__(self):
        return self.FirstName

class WorkProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

class Deposits(models.Model):
    Member=models.ForeignKey(to=Members, blank=True, null=True, on_delete=models.CASCADE)

    Date_deposit=models.DateTimeField(auto_now=True)
    Amount_deposit=models.DecimalField(max_digits=6, decimal_places=2)


    class Meta:
        verbose_name_plural = "Deposits"
    def __str__(self):
        return self.Member.FirstName


class Loans(models.Model):
    Member=models.ForeignKey(to=Members, blank=True, null=True, on_delete=models.CASCADE)

    Date_loan=models.DateTimeField(auto_now=True)
    Amount_loan=models.DecimalField(max_digits=6, decimal_places=2)


    class Meta:
        verbose_name_plural = "Loans"
    def __str__(self):
        return self.Member.FirstName




class Repayments(models.Model):
    Member=models.ForeignKey(to=Members, blank=True, null=True, on_delete=models.CASCADE)

    Date_repayment=models.DateTimeField(auto_now=True)
    Amount_repayment=models.DecimalField(max_digits=6, decimal_places=2)


    class Meta:
        verbose_name_plural = "Repayments"
    def __str__(self):
        return self.Member.FirstName
