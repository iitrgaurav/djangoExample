from django.shortcuts import render
from feedback_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'feedback_app/index.html')

def help(request):
    helpdict = {'help_me':"How to rate an Interviewer..."}
    return render(request, 'feedback_app/help.html', context=helpdict)

def feedback(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #do some code
            print("Validation success")
            print("NAME :" + user_form.cleaned_data['username'])
            print("EMAIL :" + user_form.cleaned_data['email'])
            print("TEXT :" + profile_form.cleaned_data['feedback'])

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'feedback_app/feedback.html',{'user_form':user_form,
                                                         'profile_form':profile_form,
                                                         'registered':registered,
                                                          })
