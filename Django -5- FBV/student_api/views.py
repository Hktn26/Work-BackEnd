from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def home(request):
    return Response(
        {
            "message": "Welcome to the Home Page"
        }
    )


# ------------------------------------------------------------
'''
    HTTP Request Types:
        Get -> Public verilerdir. Listeleme/Goruntuleme islemlerinde kullanilir.
        Post -> Private verilerdir. Kayit olusturma islemlerinde kullanilir. (ID'ye ihtiyac duymaz.)
        * Put -> Kayit guncelleme islemlerinde kullanilir. (Veri bir butun olarak guncellenir.) (ID'ye ihtiyac duyar.)
        * Patch -> Kayit guncelleme islemlerinde kullanilir. (Verinin sadece ilgili kismi guncellenir.) (ID'ye ihtiyac duyar.)
        * Delete -> Kayit silme islemlerinde kullanilir. (ID'ye ihtiyac duyar.)

'''
# ------------------------------------------------------------
# StudentSeralizers Tum Kayitlari Goruntuleme: serializer -> json

from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

@api_view(['GET']) # Default ['GET']
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# ------------------------------------------------------------
# StudentSeralizers Yeni Kayit Ekleme: json -> serializer

# HTTP Status Codes:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Created Successfully"
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Data not validated",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)
    

# ------------------------------------------------------------
# StudentSeralizers Tek Kayit Goruntuleme: 

from django.shortcuts import get_object_or_404

@api_view(['GET'])
def student_detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk) # Bulamadiginda Hata Gosterme 
    serializer = StudentSerializer(instance=student)
    return Response(serializer.data)

# ------------------------------------------------------------
# StudentSeralizers Tek Kayit Guncelleme: 


@api_view(['PUT']) 
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Update Successfully"
        }, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({
            "message": "Data not validated",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)
    
# ------------------------------------------------------------
# StudentSeralizers Tek Kayit Silme: 

@api_view(['DELETE'])

def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return Response({
            "message": "Delete Successfully"
        }, status=status.HTTP_204_NO_CONTENT)
    
