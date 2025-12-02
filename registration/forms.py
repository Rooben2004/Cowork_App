from django import forms
from .models import Company

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['status', 'created_at']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company name'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. IT, Staffing, SaaS'}),
            'size_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 1-10, 10-50'}),

            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact person name'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),

            'seats_required': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of seats'}),

            'space_type': forms.Select(attrs={'class': 'form-select'}),

            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'duration_months': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in months'}),

            'budget_per_seat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Budget per seat (₹)'}),

            'amenities': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Wifi, parking, meeting rooms, 24x7 access...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Tell us about your company and workspace needs...'
            }),
        }
