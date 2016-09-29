from django import forms

from .models import CSVInput

from .journalprocess.csvreader import CSVReader
import os

class CSVForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(CSVForm, self).__init__(*args, **kwargs)
    #     self.fields['csv_file'].required = True
    #


    class Meta:
        model = CSVInput
        fields = ('csv_file',)


    def save(self, commit=True):
        """ This is override method of ModelForm.

        """
        model = super(CSVForm, self).save(commit=False)
        if commit:
            model.save()

        return CSVReader(str(model.csv_file))


