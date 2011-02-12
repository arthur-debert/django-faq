from django import forms

from models import Question

class QuestionProposeForm(forms.ModelForm):
    """
    This form gives users the ability to propose own questions to be added to
    the list of frequently asked questions.
    """

    class Meta:
        model = Question
        fields = ('topic', 'question',)
    
    def __init__(self, *args, **kwargs):
        """ 
        Try to get the user's language from the middleware and only display
        those topics that conform to that language 
        """
        language = kwargs.pop("language", None)
        super(QuestionProposeForm, self).__init__(*args, **kwargs)
        self.fields['topic'].queryset = self.fields['topic'].queryset \
                                        .filter(language=language)
        # don't display the help texts
        for field in self.fields.values():
            field.help_text = None
