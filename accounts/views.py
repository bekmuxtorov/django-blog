from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import CustomUser
from .forms import CustomUserChangeForms, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserDatasView(TemplateView):
    template_name = 'user_data.html'


def BlogEditUserView(request):
    error = ""
    if request.method == "POST":
        form = CustomUserChangeForms(
            request.POST, instance=CustomUser.objects.get(id=request.user.id))
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Forma to'ldirishda xatolik!"

    form = CustomUserChangeForms(
        instance = CustomUser.objects.get(id=request.user.id))

    context = {
        "form": form,
        "error": error
    }

    return render(request, 'edit_profile.html', context)


