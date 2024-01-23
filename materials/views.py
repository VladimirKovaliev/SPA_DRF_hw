from django.shortcuts import render
from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.serializers import LessonSerializer, CourseSerializer

