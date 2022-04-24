from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    # if request.method == "POST":
    #     # request.POST['item_text'] gives us the request value associated with the key
    #     return HttpResponse(request.POST['item_text'])
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    # else:
    #     new_item_text = ' '
    # item = Item()
    # item.text =   request.POST.get('item_text', " ")
    # item.save()
    items = Item.objects.all()
    return render(request, "home.html", {'items': items})
