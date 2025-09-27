from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here.
def about_me(request):
    """
    Renders the most recent About-me page
    and allows user collaboration requests.

    Displays a single instace of :model:`about.About`.

    **Context:**

    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.

    **Template:**

    :template:`about/about_me.html`
    """
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
