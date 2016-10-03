from django.views.generic.edit import CreateView,FormView
from .models import CSVInput
from .forms import CSVForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class CSVCreateView(LoginRequiredMixin, FormView):

    form_class = CSVForm
    model = CSVInput
    template_name = "csvform.html"
    success_url = reverse_lazy('saasu:csvupload')
    success_message = "sucessfully upload"



    def form_valid(self, form):

        """
        If the form is valid, save the associated model.
        """
        self.object, self.status_list = form.save()

        for status in self.status_list:
            if status['status'] == 'Error':
                messages.add_message(
                    self.request, messages.ERROR,status['remarks'])
            else:
                messages.add_message(
                    self.request, messages.SUCCESS, status['remarks'])

        # return HttpResponseRedirect(self.get_success_url())

        return super(CSVCreateView, self).form_valid(form)

    def csv_upload(self):

        return render(self.request, 'csvform.html')

