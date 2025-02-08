from django.shortcuts import render
from django.http import JsonResponse
from .forms import RuleModelForm,AlertModelForm
from .models import RuleModel,AlertName
from pathlib import Path
from django.contrib import messages
import os
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect






def env_variable_view(request):
    if request.method == 'POST':
        form = RuleModelForm(request.POST)
        if form.is_valid():
            env_variable_name = form.cleaned_data['condition']
            # Check if an entry with the same name already exists
            # if EnvVariable.objects.filter(env_variable_name=env_variable_name).exists():
            #     messages.error(request, 'An environment variable with this name already exists.')
            # else:
            #     form.save()
            #     messages.success(request, 'Environment variable added successfully.')
            form.save()
            return redirect('env_variable_form')  
    else:
        form = RuleModelForm()

    env_variables = RuleModel.objects.all()
    return render(request, 'vectorui/env_template.html', {'form': form, 'env_variables': env_variables})

def delete_env_variable(request, id):
    variable = get_object_or_404(RuleModel, id=id)
    variable.delete()
    messages.success(request, 'Environment variable deleted successfully.')
    return redirect('env_variable_form')  

def update_env_variable(request, id):
    if request.method == 'POST':
        
        # print("---------form -------->>>>>..",form)
        variable = get_object_or_404(RuleModel, id=id)
        form = RuleModelForm(request.POST,request.FILES,instance=variable)
        if form.is_valid():
            # env_variable_name = form.cleaned_data['operation']
            # form = RuleModelForm()

            # Check if an entry with the same name already exists
            # if EnvVariable.objects.filter(env_variable_name=env_variable_name).exists():
            #     messages.error(request, 'An environment variable with this name already exists.')
            # else:
            form.save()
            #     messages.success(request, 'Environment variable added successfully.')
            # form.save()
            env_variable_name = form.cleaned_data['condition']
            env_variables = RuleModel.objects.all()
            
            return render(request, 'vectorui/env_template.html', {'form': form,'env_variables': env_variables})
  
    else:
        variable = get_object_or_404(RuleModel, id=id)
        print("---------------variable objesct------?>>>>",variable)
        form = RuleModelForm(instance=variable)

    # variable.save()
    # messages.success(request, 'Environment variable deleted successfully.')
    return render(request, 'vectorui/env_template_update.html', {'form': form})
  




def all_alerts(request):
    if request.method == 'POST':
        form = AlertModelForm(request.POST)
        if form.is_valid():
            env_variable_name = form.cleaned_data['condition']
            # Check if an entry with the same name already exists
            # if EnvVariable.objects.filter(env_variable_name=env_variable_name).exists():
            #     messages.error(request, 'An environment variable with this name already exists.')
            # else:
            #     form.save()
            #     messages.success(request, 'Environment variable added successfully.')
            form.save()
            return redirect('env_variable_form')  
    else:
        form = AlertModelForm()
    all_alerts_variables = AlertName.objects.all()
    query = request.GET.get("q", "") 
    if query:
        all_alerts_variables = all_alerts_variables.filter(Q(sensor_id__icontains=query)|Q(rule_name__icontains=query))  # Search in product name

    _type = request.GET.get("type", "")
    if _type:
        all_alerts_variables = all_alerts_variables.filter(type=_type)
    
    return render(request, 'vectorui/alert_template.html', {'form': form, 'alerts_variables': all_alerts_variables})



####################