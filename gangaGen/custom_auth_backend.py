from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()
print(User)

class AccessCodeBackend(ModelBackend):
    def authenticate(self, request, access_code=None, **kwargs):
        print(access_code)
        if access_code:
            try:
                use= User.objects.all()
                for user in use:
                    print(f"Username: {user.username}, Access Code: {user.access_code}")
                user = User.objects.get(access_code=access_code)
                print(user)
                return user
            except User.DoesNotExist:
                return None
        return None