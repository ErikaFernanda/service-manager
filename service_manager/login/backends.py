
from login.models import User
from django.contrib.auth.backends import ModelBackend
from home.models import CompanyUser


class CustomBackend(ModelBackend):

    @staticmethod
    def authenticate(username, password, company_id):
        try:
            user = User.objects.get(username__iexact=username)
            print(user.company_id)
            print(company_id)
            if user.check_password(password) and company_id==user.company_id:
                # CompanyUser.objects.get(user=user, company_id=company_id)
                
                return user
        except User.DoesNotExist:
            return None
