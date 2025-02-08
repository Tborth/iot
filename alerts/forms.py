from django import forms
from .models import RuleModel,AlertName

from django_filters.views import FilterView
import django_filters

class RuleModelForm(forms.ModelForm):
        
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            # self.fields['name'].widget.attrs.update({'class':'form-control'})
        STATUS = [
            ('High', 'high'),
            ('Low', 'low'),
            ('Critical', 'Critical'),
           
        ]
        OPERATION = [
            ('==', '='),
            ('<=', '<='),
            ('>=', '>='),
           
        ]
   
     

        condition = forms.ChoiceField(
            label="Condition",
            choices=OPERATION,
            
            widget=forms.Select(attrs={'class': 'w-full border border-gray-300 rounded-md py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600'})
        )
        status= forms.ChoiceField(
            label="Status",
            choices=STATUS,
            widget=forms.Select(attrs={'class': 'w-full border border-gray-300 rounded-md py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600'})
        )
        duration = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control border border-gray-300 rounded-md  py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600'})),
        class Meta:
            model = RuleModel
            fields = ['rule_name', 'sensor_id','field_name','condition','thrashold','duration','status']
            widgets = {
            'rule_name': forms.Textarea(attrs={'class': ' form-control border border-gray-300 rounded-md  py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600',
              'rows': 1, 'placeholder': 'Enter value'}),
            'sensor_id': forms.Textarea(attrs={'class': ' form-control border border-gray-300 rounded-md  py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600',
              'rows': 1, 'placeholder': 'Enter value'}),
            'field_name': forms.Textarea(attrs={'class': 'form-control border border-gray-300 rounded-md  py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600',
             'rows': 1, 'placeholder': 'Enter value'}),
            'condition': forms.Textarea(attrs={'class': ' form-control border border-gray-300 rounded-md  py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600',
               'rows': 1, 'placeholder': 'Enter value'}),
            'thrashold': forms.Textarea(attrs={'class': 'form-control border border-gray-300 rounded-md  py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600',
               'rows': 1, 'placeholder': 'Enter value'}),
        #     'duration': forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
        # # min_value=1,  # Minimum value allowed
        # # max_value=100  # Maximum value allowed
        #     ),
            #   quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'})),
            'status':  forms.Textarea(attrs={'class': 'form-control border border-gray-300 rounded-md  py-2 focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-green-600',
              'rows': 1, 'placeholder': 'Enter value'}),
            
            }
            def clean_thrashold(self):
                thrashold = self.cleaned_data.get("thrashold")
                if thrashold is not None  :
                    raise forms.ValidationError("Thrashold must be greater than zero.")
                return thrashold


######################################################################################################################################
class AlertFilter(django_filters.FilterSet):
    rule_name = django_filters.CharFilter(lookup_expr="icontains")  # Search by name
    type = django_filters.ChoiceFilter(choices=[("critical", "low"), ("high", "medium")])  # Dropdown filter
    sensor_id = django_filters.CharFilter(lookup_expr="icontains")
    content = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = AlertName
        fields = ['type', 'rule_name','sensor_id','content']

class AlertModelForm(FilterView):
    model = AlertName
    template_name = "alert_template.html"
    filterset_class = AlertFilter