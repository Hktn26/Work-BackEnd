from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer





# -----------------------------------------------------------------------
# https://www.django-rest-framework.org/tutorial/3-class-based-views/
#                           APIView
# -----------------------------------------------------------------------
#Listeleme:
class StudentListCreate(APIView):

    # Listele (GET Method)
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
    
    # Yeni kayit (POST Method)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class StudentDetailUpdateDelete(APIView):
    #Tek kayit goruntuleme:
    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student)
        return Response(serializer.data)
    
    #Tek kayit guncelle:
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # Tek Kayit silme:
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({"Message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

# Odev Api Viewlari birlestir.




# ------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview
#                           GenericAPIView
# ------------------------------------------------------------------------------

from rest_framework.generics import GenericAPIView

# 02.02.02