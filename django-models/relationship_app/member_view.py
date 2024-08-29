# member_view.py

from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .utils import is_member  # Assuming utils.py is in the same directory

@user_passes_test(is_member)
def member_only_view(request):
    return HttpResponse("This view is for Members only.")
