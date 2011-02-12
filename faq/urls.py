from django.conf.urls.defaults import patterns, url

from views import QuestionListView, QuestionDetailView, QuestionCreateView

urlpatterns = patterns('',
    url(r'^$', QuestionListView.as_view(), name="question-list"),
    url(r'^(?P<slug>[-\w]+)/$', QuestionDetailView.as_view(), name="question-detail"),
    url(r'^propose$', QuestionCreateView.as_view(), name="question-create"),
)
