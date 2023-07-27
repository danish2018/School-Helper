from .models import School
from django.shortcuts import render
from django.core.paginator import Paginator


def get_sorted_schhols(schools, user_latitude, user_longitude):
    school_list = list()
    for school in schools:
        school_data = dict()
        school_data['school_name'] = school.name
        school_data['school_address'] = school.address
        school_data['school_pincode'] = school.pincode
        school_data['distance'] = abs(
            user_latitude - int(school.latitude)) + abs(user_longitude - int(school.longitude))
        school_list.append(school_data)
    sorted_school_data = list(
        sorted(school_list, key=lambda data: data['distance']))

    return sorted_school_data


def search_school_view(request):
    pincode = request.GET.get('pincode')
    schools = School.objects.filter(pincode=pincode)
    user_latitude = 90
    user_longitude = 100
    sorted_schools = get_sorted_schhols(
        schools, user_latitude, user_longitude)
    paginator = Paginator(sorted_schools, 1)
    page_number = request.GET.get('page')
    sorted_schools = paginator.get_page(page_number)
    context = {
        'sorted_schools': sorted_schools,
        'pincode': pincode
    }
    return render(request, 'result.html', context)
