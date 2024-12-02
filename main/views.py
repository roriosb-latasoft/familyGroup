from django.shortcuts import render
from .models import Corredor, Propiedad

def home(request):
    # Recupera todas las propiedades y ordénalas alfabéticamente
    propiedades = Propiedad.objects.all().order_by('nombre')  # Puedes cambiar el orden como desees
    return render(request, 'home.html', {'propiedades': propiedades})

def propiedades_list(request):
    propiedades = Propiedad.objects.all()
    total_propiedades = propiedades.count()
    return render(request, 'propiedades.html', {
        'propiedades': propiedades,
        'total_propiedades': total_propiedades
    })

from django.contrib.auth.decorators import login_required, user_passes_test

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
@login_required
def crud_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'crud_propiedades.html', {'propiedades': propiedades})

@user_passes_test(is_superuser)
@login_required
def crud_corredores(request):
    corredores = Corredor.objects.all()
    return render(request, 'crud_corredores.html', {'corredores': corredores})



from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get_success_url(self):
        # Redirigir al CRUD si es superusuario, de lo contrario, al home
        if self.request.user.is_superuser:
            return '/crud/propiedades/'  # Ruta al CRUD
        return '/'

custom_login = CustomLoginView.as_view(template_name='login.html')

