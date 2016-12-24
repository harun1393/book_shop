
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from shop.models import BookInfo, Student, University
from shop.serializers import BookSerializers, StudentSerializer, UniversitySerializer
from rest_framework import viewsets
from django.views.generic import TemplateView, RedirectView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['task'] = BookInfo.objects.get(pk=self.kwargs.get('std_id', None))
        return context


class HomeRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        task_id = self.kwargs.get('std_id', None)
        student = Student.objects.get(pk=task_id)
        self.url = '/shop/%s-%s'%(student.id, student.id_no)
        return super(HomeRedirectView, self).get(self, request, *args, **kwargs)


class BookList(APIView):
    def get(self,request, format=None):
        books = BookInfo.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListView(TemplateView):
    template_name = ''


class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializers(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        print (book)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


