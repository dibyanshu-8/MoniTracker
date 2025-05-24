from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from moniapp import models
from.models import Account,Expense
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView 
from datetime import datetime

# Create your views here.

