import csv

from django.shortcuts import render

# Create your views here.

import json

import datetime

import decimal

from django.http import JsonResponse

from django.http import HttpResponse

from django.shortcuts import redirect

from django.template import loader

from django.contrib.auth.decorators import login_required

from .upc import UpcWalmart

from .objects_behevior import User

from django.contrib import messages


@login_required
def index(request):
    if request.method == 'GET':
        template = loader.get_template('plots/index.html')
        context = {'product_header': UpcWalmart.get_header_upc()}
        return HttpResponse(template.render(context, request))


@login_required
def data_array(request):
    """ Data for datateble """

    class JSONEncoder(json.JSONEncoder):
        """ Fix error """

        def default(self, o):
            """
            Args:
              o:
            Returns:
            """
            if isinstance(o, decimal.Decimal):
                return float(o)
            if isinstance(o, (datetime.datetime, datetime.date)):
                return str(o)
            return json.JSONEncoder.default(self, o)

    draw = int(request.GET['draw'], base=0) + 1
    user = User(request.user)
    data = user.get_upc_limit_sort(int(request.GET['start']), int(request.GET['length']),\
                                   request.GET['columns[' + request.GET['order[0][column]'] + '][data]'],\
                                   (-1, 1)[request.GET['order[0][dir]'] == 'asc'])
    data = json.dumps({"draw": draw,
                       "recordsTotal": user.count_upc(),
                       "recordsFiltered": user.count_upc(),
                       "data": data}, cls=JSONEncoder)

    return HttpResponse(data)


@login_required
def add_upc(request):
    """ Add walmart object """

    user = User(request.user)
    if user.set_upc(request.GET['upc']) != 1:
        messages.info(request, "Wrong upc or key!")
    return redirect("index")


@login_required
def del_upc(request):
    """ Delete walmart object  """
    user = User(request.user)
    user.del_upc(str(request.GET['delete']))
    return redirect("index")


@login_required
def add_file_csv(request):
    """ Add upc from csv  """
    if request.method == 'POST':
        user = User(request.user)
        err_key = user.set_csv(request.FILES.get('file').read())
        if err_key == -1:
            messages.error(request, "File Error")
            return redirect("index")
        if len(err_key) > 0:
            messages.info(request, "Wrong upc " + str(len(err_key)))
        return redirect("index")
    messages.error(request, "File Error")
    return redirect("index")


@login_required
def add_key(request):
    """ Add key walmart """

    user = User(request.user)
    key = request.GET['key']
    user.set_key(key)
    return redirect("index")


def download_example(request):
    """ Return csv example """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="example.csv"'
    writer = csv.writer(response)
    writer.writerow(['upc'])
    writer.writerow(['035000521019'])
    writer.writerow(['10001137891'])
    return response


@login_required
def download(request):
    """ Walmart data in csv format  """
    user = User(request.user)
    response = HttpResponse(user.get_csv(),content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="database.csv"'
    return response


@login_required
def settings(request):
    """ Return Settings.html and key user"""
    user = User(request.user)
    template = loader.get_template('plots/setting.html')
    if request.method == 'POST':
        user = User(request.user)
        if(user.set_key(request.POST['key']) == -1):
            messages.error(request, "Key Error")
        context = {'key': user.key_walmart()}
        return HttpResponse(template.render(context, request))
    elif request.method == 'GET':
        context = {'key': user.key_walmart()}
        return HttpResponse(template.render(context, request))






