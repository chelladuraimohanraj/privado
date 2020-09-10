from django.shortcuts import render
from django.http import JsonResponse
import pymongo
from pprint import pprint
# Create your views here.
def home(req):
    return render(req,'home.html')

def isint(x):
    try:
        if int(x):
            return True
    except ValueError:
        return False

def insert_retrive(req,customer_id):
    if isint(customer_id):
        if req.method=='POST':
            client=pymongo.MongoClient()
            db=client['te']
            templates=db['templates']
            final_list=[]
            new_fields=templates.find_one({'type':'system'})
            new_fields['type']='customer'
            new_fields['customerId']=customer_id
            for customertemplate in templates.find({'type':'customer'}):
                if customertemplate['customerId']==customer_id:
                    return JsonResponse({'status':'500 customer already exists'})
            for systemtemplate in templates.find({'type':'system'}):
                final_list.extend(systemtemplate['fields'])

            new_fields['fields']=final_list
            pprint(new_fields)
            new_fields.pop('_id')
            templates.insert_one(new_fields)
            return JsonResponse({'status':'200 success'})
        if req.method=='GET':
           
            client=pymongo.MongoClient()
            db=client['te']
            templates=db['templates']
            for customertemplate in templates.find({'type':'customer'}):
                if customertemplate['customerId']==customer_id:
                    customertemplate.pop('_id')
                  
                    return JsonResponse({'status':'200 success','data':customertemplate})
            return JsonResponse({'status':'404 no such customer','data':'none'})
    else:
        return JsonResponse({'status':'404 Customer id must be integer'})