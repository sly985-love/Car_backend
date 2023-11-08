from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from .resources import OderResource
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models


# def export(request):
#     oder_resource = OderResource()
#     dataset = oder_resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment;filename="oders.xls"'
#     return response


class LoginView(APIView):

    def get(self, request, *args, **kwargs):
        phone = request.query_params.get('phone')
        carno = request.query_params.get('carno')
        date = request.query_params.get('date')
        time = request.query_params.get('time')
        come = request.query_params.get('visit')
        localpath = request.query_params.get('address')
        print(phone)
        print(carno)
        print(date)
        print(time)
        print(come)
        print(localpath)
        models.Oder.objects.create(telephone=phone, car_number=carno, appointment_date=date, appointment_time=time,
                                   visit=come, address=localpath)
        return Response({"status": True})


# from django import forms
#
#
# class OderForm(forms.Form):  # 定义的django表单
#     telephone = forms.CharField()
#     car_number = forms.CharField()
#     appointment_date = forms.CharField()
#     appointment_time = forms.CharField()
#     visit = forms.CharField()
#     address = forms.CharField()
