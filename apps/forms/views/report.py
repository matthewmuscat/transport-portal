from apps.forms.forms import ReportForm
from django.shortcuts import render
from django.views import View


class Report(View):
    def get(self, request):
        form = ReportForm()
        return render(request, "forms/report.html", {"report_form": form})
