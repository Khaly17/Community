from django.shortcuts import render
from .forms import MemberForm
from membres.models import Member
from django.contrib import messages


def homepage(request):

    if request.method == 'POST':
        form = MemberForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            form = MemberForm()

            messages.success(request, "Merci pour votre inscription !")

    else:
        form = MemberForm() # le formulaire à afficher sur la page

    return render(request, 'membres/index.html', {'form': form})

def member_view(request, member_id):
    mb = Member.objects.filter(id=member_id)
    return render(request, 'membres/member_view.html',  {'mb': mb})

def members_view(request):
    mbs = Member.objects.all()
    return render(request, 'membres/members_view.html',  {'mbs': mbs})