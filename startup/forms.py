from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("fired_date", "fired", "profession", "full_name", "name", "email",)
        fields = ("name", "email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("fired_date", "fired", "profession", "full_name", "name", "email",)


