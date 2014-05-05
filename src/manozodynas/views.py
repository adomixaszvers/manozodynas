from django.shortcuts import render
from .models import Word
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


def index_view(request):
    return render(request, 'manozodynas/index.html', {})
def zodziai_view(request):
    zodziai = Word.objects.all()
    return render(request, 'manozodynas/zodziai.html', {"zodziai": zodziai})

class PridetiZodi(CreateView):
    model = Word
    template_name = "manozodynas/pridetizodi.html"
    success_url = reverse_lazy('zodziai')
