from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(
        request, "taskwallet/templates/index.html", context={"date": datetime.today()}
    )


def services(request):
    return render(request, "taskwallet/templates/services.html")


def connexion(request):
    return render(request, "taskwallet/templates/connexion.html")


def email_sent(request):
    return render(request, "taskwallet/templates/email_sent.html")


# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)  # ajout d’un nouveau formulaire ici

#         print("La méthode de requête est : ", request.method)
#         print("Les données POST sont : ", request.POST)
#         # if form.is_valid():
#         #     send_mail(
#         #         subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
#         #         message=form.cleaned_data["message"],
#         #         from_email=form.cleaned_data["email"],
#         #         recipient_list=["victoriasugili18@gmail.com"],
#         #     )
#         return redirect("accueil")
#     else:
#         form = ContactForm()
#     return render(
#         request, "taskwallet/templates/contact.html", {"form": form}
#     )  # passe ce formulaire au gabarit
