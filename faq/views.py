from datetime import datetime

# Try to get the cbv classes from django, then from django-cbv for compatibility
try:
    from django.views.generic import ListView, DetailView, CreateView
except ImportError:
    from cbv.views.list import ListView
    from cbv.views.detail import DetailView
    from cbv.views.edit import CreateView

from django.template.defaultfilters import slugify

import enums
from models import Question
from forms import QuestionProposeForm

class QuestionListView(ListView):
    model = Question
    context_object_name = "question_list"
    queryset = Question.objects.active()

    def get_query_set(self):
        """ 
        Only show protected questions when user is logged in
        """
        if not self.request.user:
            return self.queryset.exclude(protected=True)
        return self.queryset

    def get_context_data(self, **kwargs):
        """ 
        Add a few infos to the template's context
        """
        context = super(QuestionListView, self).get_context_data(**kwargs)

        # get timestamp of latest update of all displayed questions
        updates = self.get_queryset().values("updated_on").order_by("-updated_on")
        if len(updates) > 0:
            context["last_update_on"] = updates[0]["updated_on"]

        # get count of all topics so that the template knows whether there's
        # need to display topics at all
        context["topic_num"] = len(set([q.topic for q in self.get_queryset()]))

        return context

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = "question"
    queryset = Question.objects.active()


class QuestionCreateView(CreateView):
    model = Question
    context_object_name = "question"
    success_url = "/faq/"
    form_class = QuestionProposeForm

    def get_form_kwargs(self, *args, **kwargs):
        """
        Add ``LANGUAGE_CODE`` to the form's kwargs so that the topics can be
        displayed accordingly.
        """
        kwargs = super(QuestionCreateView, self).get_form_kwargs()
        kwargs["language"] = self.request.LANGUAGE_CODE
        return kwargs

    def form_valid(self, form):
        now = datetime.now()
        q = form.save(commit=False)
        slug = slugify("%s-%s" % (q.question, now))
        q.slug = slug
        q.language = self.request.LANGUAGE_CODE
        q.status = enums.STATUS_PROPOSED
        q.created_by = self.request.user
        return super(QuestionCreateView, self).form_valid(form)
