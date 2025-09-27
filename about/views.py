from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here.
def about_me(request):
    about = About.objects.order_by("-updated_on").first()
    # about = get_object_or_404(queryset)
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save(commit=False)
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! \
                 I endeavour to respond within 2 working days."
            )

    collaborate_form = CollaborateForm

    return render(
        request,
        "about/about_me.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
