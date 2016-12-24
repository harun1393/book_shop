from django.conf.urls import url
from shop.views import StudentViewSet, UniversityViewSet, BookList, BookDetail, HomeView, HomeRedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.views.generic import TemplateView, ListView
from shop.models import BookInfo

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'university', UniversityViewSet)




urlpatterns = [
    url(r'^books/$',BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', BookDetail.as_view()),
    url(r'^home/$', TemplateView.as_view(template_name='index.html')),
    url(r'^(?P<std_id>\d+)/$', HomeRedirectView.as_view()),
    url(r'^(?P<std_id>\d+)-(?P<id_no>[0-9]+)/$', HomeView.as_view()),
    url(r'^$', ListView.as_view(
        model=BookInfo,
        paginate_by='5',
        queryset=BookInfo.objects.all(),
        context_object_name="book_list",
        template_name='index.html',

    )),
]

urlpatterns += router.urls
#urlpatterns = format_suffix_patterns(urlpatterns)