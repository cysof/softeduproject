from django.shortcuts import render
from projectStore.forms import ContactForm
from projectStore .views import Department

def home(request):
    return render(request, 'contactus/home.html')


def contactuspage(request):
    dept = Department.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title =form.cleaned_data['title']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            form.save()
            return render(request, 'contactus/success.html')
    form = ContactForm()
    context = {'form': form,
            'dept': dept}
    return render(request, 'contactus/contactform.html', context)







def hirewriter(request):
    return render(request, 'contactus/hire.html')