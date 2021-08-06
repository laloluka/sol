from django.contrib import admin

# Register your models here.
from .models import Deposits,Members, Loans, Repayments,WorkProcess



class DepositAdmin(admin.ModelAdmin):
    list_display = ("Member","Amount_deposit","Date_deposit")

class MemberAdmin(admin.ModelAdmin):
    list_display = ("AccountNumber","FirstName","LastName","Date_start","Base_fund")
    ordering=("AccountNumber",)
    search_fields=("AccountNumber","LastName",)


class LoanAdmin(admin.ModelAdmin):
    list_display = ("Member","Amount_loan","Date_loan")


class Workprocessdmin(admin.ModelAdmin):
    list_display = ("text","approved")





class RepaymentAdmin(admin.ModelAdmin):
    list_display = ("Member","Amount_repayment","Date_repayment")
admin.site.register(Repayments,RepaymentAdmin)
admin.site.register(Members,MemberAdmin)
admin.site.register(Deposits,DepositAdmin)
admin.site.register(Loans,LoanAdmin)
admin.site.register(WorkProcess,Workprocessdmin)
admin.site.site_header="SOL Credit Union Admin Panel"