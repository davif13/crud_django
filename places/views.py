from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Places
from django.utils import timezone


def index(request, important_message=None):
    place_list = Places.objects.order_by('-create_date')
    context = {'place_list': place_list}
    return render(request, 'places/index.html', context)


def detail(request, place_id=''):
    place_selected = {"id": ''}
    if(place_id != ''):
        place_selected = Places.objects.get(id=place_id)

    return render(request, 'places/detail.html', {'place': place_selected})


def delete(request, place_id):
    try:
        place2Delete = Places.objects.get(pk=place_id)
        place2Delete.delete()
        return render(request, 'places/delete.html', {
            'place': place2Delete,
            'important_message': "Your place has been deleted successfully",
        })
    except (KeyError, Places.DoesNotExist):
        return render(request, 'places/delete.html', {
            'place': place2Delete,
            'important_message': "could not delete your place.",
        })


def upsert(request):
    _id = request.POST['id']
    _name = request.POST['name']

    if(_id == ''):
        try:
            newPlace = Places(name=_name, create_date=timezone.now())
            newPlace.save()
            return render(request, 'places/detail.html', {
                'place': newPlace,
                'important_message': "Your place has been saved",
            })
        except (KeyError, Places.DoesNotExist):
            return render(request, 'places/detail.html', {
                'place': newPlace,
                'important_message': "could not save your new place.",
            })

    else:
        try:
            place2Update = Places.objects.get(pk=_id)
            place2Update.name = _name
            place2Update.save()
            return render(request, 'places/detail.html', {
                'place': place2Update,
                'important_message': "Your place has been updated successfully",
            })
        except (KeyError, Places.DoesNotExist):
            return render(request, 'places/detail.html', {
                'place': newPlace,
                'important_message': "could not update your new place.",
            })
