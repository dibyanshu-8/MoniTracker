from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    long_term=forms.BooleanField(required=False)
    
    
    class Meta:
        model=Expense
        fields=['name','amount','interest_rate','date','end_date','long_term']
        
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'interest_rate':forms.NumberInput(attrs={'class':'form-control'}),
            'end_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'long_term':forms.CheckboxInput(attrs={'class':'form-control'}),
        }