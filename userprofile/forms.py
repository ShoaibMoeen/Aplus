from allauth.account.forms import SignupForm
from userprofile.models import UserProfile
from django import forms

class MySignUpForm(SignupForm):

    def save(self, request):

        user= super(MySignUpForm, self).save(request)
        userprofile= UserProfile.objects.get(user=user)
        userprofile.phone_no= request.POST.get("phone_no")
        userprofile.full_name= request.POST.get("full_name")
        userprofile.save()
        return user
