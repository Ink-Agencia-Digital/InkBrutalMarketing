from django_registration.forms import RegistrationForm
from apps.Administrador.models import CustomUser

class CustomUserForm(RegistrationForm):
    
    class Meta(RegistrationForm.Meta):
        model = CustomUser