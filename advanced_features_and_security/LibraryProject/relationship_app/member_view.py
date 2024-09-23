from .test_func import is_member
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

@user_passes_test(is_member)
def member_only_view(request):
    return HttpResponse("This view is for Members only.")