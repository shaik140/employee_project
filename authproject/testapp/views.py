from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')
@login_required
def java_exams_view(request):
    return render(request,'testapp/javaexams.html')
@login_required
def python_exams_view(request):
    return render(request,'testapp/pythonexams.html')
@login_required
def apptitude_exams_view(request):
    return render(request,'testapp/apptitudeexams.html')
def logout_view(request):
    return render(request,'testapp/logout.html')


def login_page(request):
    return render(request,'testapp/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            return HttpResponseRedirect('/accounts/login')
    else:
        form = SignUpForm()
    return render(request, 'testapp/signup.html', {'form': form})
