# admin_view.py

from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .test_func import is_admin, is_member, is_librarian  # Assuming utils.py is in the same directory

@user_passes_test(is_admin)
def admin_only_view(request):
    return HttpResponse("This view is for Admins only.")

@user_passes_test(is_member)
def member_only_view(request):
    return HttpResponse("This view is for Members only.")


@user_passes_test(is_librarian)
def librarian_only_view(request):
    return HttpResponse("This view is for Librarians only.")
