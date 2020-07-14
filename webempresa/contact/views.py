from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    #print("Tipo de peticion: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                "Molletes: nuevo mensaje informa que",
                "de {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["ramos.castaneda@dgeb.gob.mx"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #algo salio mal
                return redirect(reverse('contact')+"?fail")
    
    return render(request,"contact/contact.html",{'form':contact_form})