from django.forms import ModelForm
from .models import Members

class MemberForm(ModelForm):
    class Meta:
        model=Members
        fields='__all__'