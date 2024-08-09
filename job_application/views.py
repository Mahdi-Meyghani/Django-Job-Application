from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["fname"]
            last_name = form.cleaned_data["lname"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            msg_body = (f"{first_name}, your new job was submitted, congratulation :)\n"
                        f"Here is your info:\n"
                        f"{first_name}\n"
                        f"{last_name}\n"
                        f"{date}\n"
                        f"{occupation}")
            email_message = EmailMessage(subject="Job Form Submission Confirmation",
                                         body=msg_body,
                                         to=[email])
            email_message.send()

            messages.success(request, "WOW! Information submitted successfully :)")

    return render(request, "index.html")
