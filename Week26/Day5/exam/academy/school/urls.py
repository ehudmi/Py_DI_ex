from django.urls import path
from .views import TeacherList, SchoolFacilityList, LaboratoryList, course_details

urlpatterns = [
    path("teachers/", TeacherList.as_view(), name="teachers"),
    path("facilities/", SchoolFacilityList.as_view(), name="facilities"),
    path("laboratories/", LaboratoryList.as_view(), name="laboratories"),
    path("course_details/<int:id>", course_details, name="course_details"),
]
