from .test_func import is_admin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

@user_passes_test(is_admin)
def admin_only_view(request):
    return HttpResponse("This view is for Admins only.")