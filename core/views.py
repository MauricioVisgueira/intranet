from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from funcionarios.models import Funcionario

@login_required
# Create your views here.
def home(request):
    usuario = request.user
    return render(request, 'core/index.html')
