from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail



def home(request):
    return render(request, 'home.html')


def forgot(request):
	return render(request,'forgotpassword.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            auth_login(request, user)  
            return redirect(home)  
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')

    return render(request, 'loginpage.html')  

def signup_view(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')  # Corrected the typo
            
            # Create the user
            user = User.objects.create_user(username=username, password=password, email=email)
            
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to login after signup
        
        return render(request, 'signup.html')  # Render signup page for GET requests
    except Exception as e:
        print(e)

def logout(request):
	logout(request)
	groups=Group.objects.all().values()
	return redirect('')


def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")

        try:
            user = User.objects.get(username=username, email=email)
            # Generate a random password
            new_password = get_random_string(length=12)
            user.set_password(new_password)
            user.save()

            # Send the new password via email
            send_mail(
                'Your New Password',
                f'Your new password is: {new_password}',
                'from@example.com',  # Replace with your sender email
                [email],
                fail_silently=False,
            )

            messages.success(request, 'A new password has been sent to your email.')
            return redirect('login')  # Redirect to the login page

        except User.DoesNotExist:
            messages.error(request, 'Invalid username or email.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return render(request, 'loginpage.html')

		