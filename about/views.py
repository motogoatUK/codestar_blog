from django.shortcuts import render, get_object_or_404
from .models import About


# Create your views here.
def about_me(request):
    about = About.objects.order_by("-updated_on").first()
    # about = get_object_or_404(queryset)
    return render(
        request,
        "about/about_me.html",
        {"about": about},
    )
