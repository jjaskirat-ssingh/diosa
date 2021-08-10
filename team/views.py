from django.shortcuts import get_object_or_404, render


from .models import Member

def index(request):
    team = Member.objects.order_by('pass_year').filter(in_office=True)

    context = {
        'team': team
    }

    return render(request, 'pages/index.html', context) 

def Member(request, Member_id):
    Member = get_object_or_404(Member, pk=Member_id)

    context = {
    'Member': Member
    }

    return render(request, 'pages/index.html', context) 

