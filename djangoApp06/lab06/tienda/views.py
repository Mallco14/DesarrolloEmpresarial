from multiprocessing import context
from django.shortcuts import get_object_or_404,render

from .models import Producto, Categoria
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria_list = Categoria.objects.all()
    context = {'product_list': product_list,'categoria_list':categoria_list}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categoria_list = Categoria.objects.all()
    return render(request, 'producto.html',{'producto': producto,'categoria_list':categoria_list })

def detalles(request, categoria_id):
    lista_productos = get_object_or_404(Categoria, pk=categoria_id)
    categoria_list = Categoria.objects.all()
    context={
        'lista_productos':lista_productos,
        'categoria_list':categoria_list

    }
    return render(request, 'detalles.html',context)