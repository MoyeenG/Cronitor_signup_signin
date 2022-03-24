from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models


# Create your views here.

signup_obj_models = models.Signup()

def user_signup(request):
    if request.method == 'GET':
        signup_obj_form = forms.Signup()
        context = {'signup_form': signup_obj_form}
        return render(request, "signup_tmpl.html", context)

    #Create Signup details of user in db
    if request.method == 'POST':
        form_obj1 = forms.Signup(request.POST)
        if form_obj1.is_valid():
            if models.Signup.objects.all():
                for i in range(len(models.Signup.objects.all())):
                    q_dic = models.Signup.objects.all()
                    q_dic_iter = list(q_dic.values())
                    # Check for duplicate email Sign UP (Accept/Reject)
                    for user in (q_dic_iter):
                        print(type(user))
                        if request.POST.get("email") == user["email"]:
                            return HttpResponse("This email is already registered. Enter another email")
            signup_obj_models.name = request.POST.get("name")
            signup_obj_models.email = request.POST.get("email")
            signup_obj_models.password = request.POST.get("password")
            signup_obj_models.save()
            return HttpResponse("Sign UP Successful")
        return HttpResponse("Sign UP Failed")


def user_signin(request):
    if request.method == 'GET':
        signin_obj_form = forms.Signin()
        context = {'signin_form': signin_obj_form}
        return render(request, "signin_tmpl.html", context)

    # Create logged in user in db, after user authorization
    if request.method == 'POST':
        signin_obj_models = models.Signin()
        form_obj2 = forms.Signin(request.POST)
        if form_obj2.is_valid():
            if models.Signup.objects.all():
                q_dic2 = models.Signup.objects.all()
                q_dic2_iter = list(q_dic2.values())
                #User Authorization Logic
                for user in q_dic2_iter:
                    if (request.POST.get("email") == user["email"] and request.POST.get("password") == user["password"]):
                        signin_obj_models.email = request.POST.get("email")
                        signin_obj_models.password = request.POST.get("password")
                        signin_obj_models.save()
                        return HttpResponse("Login Successful")
        return HttpResponse("Login Failed")
