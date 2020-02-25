from django.http import HttpResponse
from medicSearch.models import Profile, Speciality

def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")

    medics = Profile.objects
    if name is not None:
        medics = medics.filter(user__first_name__contains=name)
    if speciality is not None:
        medics = medics.filter(specialties__name__contains=speciality)

    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)
    else:
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)

    print(medics.order_by('user__date_joined').all())
    return HttpResponse('Listagem de 1 ou mais médicos')

def list_medic_view(request, id):
    medics = Profile.objects.filter(role=2, id=id).first()
    try:
        profile = Profile.objects.filter(user__id=3).first()
        profile.user.delete()
    except Exception as e:
        print("Um erro ocorreu ao deletar um usuário. Descrição %s" % e)
    return HttpResponse('Listagem perfil de 1 médico')