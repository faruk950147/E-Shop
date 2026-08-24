from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _


class HomeView(View):

    def get(self, request):
        message = _("Hello, world!")

        return render(request, "store/home.html", {"message": message})