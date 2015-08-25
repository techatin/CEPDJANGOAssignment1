from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import UserForm, UserProfileForm


@csrf_exempt
def registration(request):

    registered = False
    
    try:

        if request.method == 'POST':
        
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():

                user = user_form.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']

                profile.save()

                registered = True
            
                return redirect('/accounts/login/')

            else:
                print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()

            return render(request,
                'accounts/register.html',
                {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
                
    except Exception as err:
        
        print err
            
