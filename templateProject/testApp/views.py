import datetime
from django.shortcuts import render

# Create your views here.

def tempview(request):
    date = datetime.datetime.now()
    my_dict = {"date_msg":date}
    return render(request,'testApp/wish.html',context=my_dict)