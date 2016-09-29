from django.views.generic.edit import CreateView
from .models import CSVInput
from .forms import CSVForm
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse


class CSVCreateView(CreateView):
    form_class = CSVForm
    model = CSVInput
    template_name = "csvform.html"
    success_url = reverse_lazy('saasuweb:csvupload')

    # fields = ['csv_file']



