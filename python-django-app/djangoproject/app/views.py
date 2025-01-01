from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

# Create your views here.

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Item.objects.create(name=name, description=description, price=price)
        return redirect('item_list')
    return render(request, 'item_form.html')

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.price = request.POST['price']
        item.save()
        return redirect('item_list')
    return render(request, 'item_form.html', {'item': item})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})
