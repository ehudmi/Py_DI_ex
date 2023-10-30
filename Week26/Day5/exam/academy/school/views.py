from django.shortcuts import render
from .models import Course, Teacher, SchoolFacility, Laboratory
from rest_framework.generics import ListAPIView
from .serializers import (
    TeacherSerializer,
    SchoolFacilitySerializer,
    LaboratorySerializer,
)


def course_details(request, id):
    course = Course.objects.get(id=id)
    return render(request, "course_details.html", {"course": course})


class TeacherList(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SchoolFacilityList(ListAPIView):
    queryset = SchoolFacility.objects.all()
    serializer_class = SchoolFacilitySerializer


class LaboratoryList(ListAPIView):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer
