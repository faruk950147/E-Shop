from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _, get_language
from .models import Category


class HomeView(View):

    def get(self, request):
        current_lang = get_language()
        message = _("Hello, world!")

        return render(request, "store/home.html", {"current_lang": current_lang, "message": message})