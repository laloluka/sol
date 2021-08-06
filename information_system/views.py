from django.shortcuts import render, redirect
import csv
from django.http import HttpResponse

from django.template.loader import render_to_string
# from weasyprint import HTML
# Create your views here.

from .models import Members, Loans, Deposits
from django.db.models import Avg, Sum
from .forms import MemberForm


def home(request):


    total_dep = Deposits.objects.aggregate(mytotal=Sum('Amount_deposit'))
    total_loan = Loans.objects.aggregate(myloan=Sum('Amount_loan'))
    maximum_dep = Deposits.objects.aggregate(mymax=Avg('Amount_deposit'))
    member_list=Members.objects.all()
    total_members=member_list.count()


    context={'member_list':member_list,'total_members':total_members,'total_dep':total_dep,'maximum_dep':maximum_dep,'total_loan':total_loan}
    return render(request,'information_system/home.html',context)



def members(request,pk):

    members=Members.objects.get(id=pk)
    deposits=Deposits.objects.get(id=pk)
    deposit = members.deposits_set.all()
    deptotal=deposits.Amount_deposit
    # myFilter=MemberFilter(request., qs=deposit)
    # deposit=myFilter.qs


    dep_count=deposit.count()

    fname_by=members.FirstName
    lname_by=members.LastName
    dep_by=fname_by+lname_by

    dep_amount=deposits.Amount_deposit
    total_depos = Deposits.objects.aggregate(mytotal=Sum('Amount_deposit'))
    context={'members':members,'dep_amount':dep_amount,'dep_by':dep_by,'deposit':deposit,'total_depos':total_depos,'deptotal':deptotal}
    return render(request,'information_system/Members.html',context)

def export(request):
    response=HttpResponse(content_type='text/csv')
    writer=csv.writer(response)
    writer.writerow(['Account Number','First Name','Last Name','Date_start'])
    for member in Members.objects.all().values_list('AccountNumber','FirstName','LastName','Date_start'):
        writer.writerow(member)
    response['Content-Disposition'] = 'attachment; filename="Member_List.csv"'
    return response






def update(request, pk):
    member=Members.objects.get(id=pk)
    form=MemberForm(instance=member)
    if request.method == 'POST':
        form=MemberForm(request.Post, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/')
    # if form.is_valid():
    #     form.save()
    #     return redirect('/')
    context = {'form':form}
    return render(request,'information_system/memberform.html',context)




def loan(request):
    loan_list=Loans.objects.all()
    total_loans=loan_list.count()
    context={'total_loans':total_loans,'loan_list':loan_list}
    return render(request,'information_system/loan.html',context)
def deposit(request):
    deposit_list=Deposits.objects.all()
    ##To get total deposit
    total_dep = Deposits.objects.aggregate(mytotal=Sum('Amount_deposit'))
    maximum_dep=Deposits.objects.aggregate(mymax=Avg('Amount_deposit'))
    # # Book.objects.all().aggregate(Avg('price'))
    # averaged=Deposits.objects.aggregate(Avg('Amount_deposit'))
    # print(averaged.values)
    #
    # Total_amount_deposit = Deposits.objects.all().aggregate(Sum('Amount_deposit'))
    # # Product.objects.all().aggregate(Sum('price'))
    # total_deposit=deposit_list.count()
    # myaverage=Deposits.objects.aggregate(avg=Avg('Amount_deposit'))
    context={'total_dep':total_dep,'maximum_dep':maximum_dep,'deposit_list':deposit_list}
    return render(request,'information_system/Deposit.html',context)
