from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import SliderCms
from price.models import PriceCard, PriceTable
from telegbot.sendmessage import sendTelegram

# Create your views here.
def index_page(request):
    sliders = SliderCms.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    render_dict= {'form':form, 'sliders':sliders, 'price_table': price_table,'pc_1':pc_1, 'pc_2':pc_2, 'pc_3':pc_3,}
    return render(request, './index.html', render_dict)

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        Order.objects.create(order_name = name, order_phone = phone)
        sendTelegram(tg_name = name,tg_phone= phone)
        return render(request, './thanks.html', {'name':name, 'phone':phone})
    else:
        return render(request, './thanks.html')

#