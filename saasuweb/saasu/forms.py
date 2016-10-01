from django import forms

from .models import CSVInput

from journalprocess.csvreader import CSVReader

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


            # print("*********")
            # print('****')
            # # print(os.path.join(model.csv_file.url))
            # csv_path = "saasuweb/{}".format(model.csv_file.url)

            """ to insert foreign key csv_object=model"""
            csv_insert = CSVReader(csv_path=model.csv_file.path, csv_object=model)
            return model, csv_insert.get_journal_and_insert()

            # print("insert")
            # print csv_insert.get_journal_and_insert()
            # print model
            # return {"model": model.id,
            #         "status": csv_insert.get_journal_and_insert()}
            #

            # return model
