from Tool.models import *
from Tool.serializers import *
from rest_framework.generics import *

class ListStudentsOfCourse(ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(
            optedCourses__id=self.kwargs['c_id']            
        )

class DetailStudentOfCourse(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        conditions = {
            'optedCourses__id': self.kwargs['c_id'],
            'id': self.kwargs['s_id']
        }
        return get_object_or_404(queryset, **conditions)

class ListStudents(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class DetailStudent(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 's_id'