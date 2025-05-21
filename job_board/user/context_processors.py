# myapp/context_processors.py
from .models import Applicant, Company

def user_role(request):
    user = request.user
    if user.is_authenticated:
        try:
            applicant = Applicant.objects.get(user=user)
            return {'is_applicant': True, 'is_company': False}
        except Applicant.DoesNotExist:
            pass
        
        try:
            company = Company.objects.get(user=user)
            return {'is_applicant': False, 'is_company': True}
        except Company.DoesNotExist:
            pass
        
    return {'is_applicant': False, 'is_company': False}
