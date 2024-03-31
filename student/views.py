# Create your views here.

import json

from django.db import connection
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from student import models
from student.models import Student
from student.utils.form import StudentForm


def get_studentsall(request):
    try:
        # 获取所有信息
        studen_obj = Student.objects.all().values()
        # 转换成为list
        studens = list(studen_obj)
        # 返回json格式
        return JsonResponse({"code": 200, "data": studens})
    except Exception as e:
        return JsonResponse({"code": 400, "msg": "错误" + str(e)})


def query_studnets(request):
    # 获取接受到的数据
    # request的body方法获取的是所有请求体的二进制数据
    # json_body = request.body
    # print(json_body)
    # 把请求体的二进制数据转换为json格式
    # json_data = json.loads(json_body)
    # print(json_data)
    # get方法键值对方式获取值
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    try:
        # 获取所有信息
        studen_obj = Student.objects.filter(
            Q(sno__icontains=data['inputstr']) |
            Q(name__icontains=data['inputstr']) |
            Q(gender__icontains=data['inputstr']) |
            Q(mobile__icontains=data['inputstr']) |
            Q(email__icontains=data["inputstr"]) |
            Q(address__icontains=data['inputstr'])

        ).values()
        studens = list(studen_obj)
        print(studens)
        # 返回json格式
        return JsonResponse({"code": 200, "data": studens})

    except Exception as e:
        return JsonResponse({"code": 400, "msg": "查询错误"})


def is_exsits_son(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_students = Student.objects.filter(sno=data['sno'])
        if obj_students.count() == 0:
            return JsonResponse({'code': 200, 'exsits': False})
        else:
            return JsonResponse({'code': 200, 'exsits': True})
    except Exception as e:
        return JsonResponse({'code': 400, 'msg': "校验失败"} + str(e))


def add_student(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_studen = Student(sno=data['sno'], name=data['name'], birthday=data['birthday'], mobile=data['mobile'],
                             email=data['email'], address=data['address'], gender=data['gender'])
        obj_studens = obj_studen.save()

        studen_obj = Student.objects.all().values()
        # 转换成为list
        studens = list(studen_obj)
        # get_studentsall()
        return JsonResponse({"code": 200, "data": studens})
    except Exception as e:
        return JsonResponse({'code': 400, 'msg': "添加到数据库失败" + str(e)})


def add_studentform(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    try:
        obj_studen = Student(sno=data['sno'], name=data['name'], birthday=data['birthday'], mobile=data['mobile'],
                             email=data['email'], address=data['address'], gender=data['gender'])
        obj_studens = obj_studen.save()

        studen_obj = Student.objects.all().values()
        # 转换成为list
        studens = list(studen_obj)
        # get_studentsall()
        return JsonResponse({"code": 200, "data": studens})
    except Exception as e:
        return JsonResponse({'code': 400, 'msg': "添加到数据库失败" + str(e)})


def update_student(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    try:
        # sno = data['sno'],
        # name = data['name'],
        # gender = data['gender'],
        # birthday = data['birthday'],
        # mobile = data['mobile'],
        # email = data['email'],
        # address = data['address']
        obj_studen = Student.objects.get(sno=data['sno'])

        obj_studen.name = data['name']
        obj_studen.gender = data['gender']
        obj_studen.birthday = data['birthday']
        obj_studen.email = data['email']
        obj_studen.mobile = data['mobile']
        obj_studen.address = data['address']

        obj_studen.save()
        studen_obj = Student.objects.all().values()
        # 转换成为list
        studens = list(studen_obj)
        # get_studentsall()
        return JsonResponse({"code": 200, "data": studens})
    except Exception as e:
        return JsonResponse({'code': 400, 'msg': "添加到数据库失败" + str(e)})


def delete_student(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_studen = Student.objects.get(sno=data['sno'])
        obj_studen.delete()
        studen_obj = Student.objects.all().values()
        # 转换成为list
        studens = list(studen_obj)
        # get_studentsall()
        return JsonResponse({"code": 200, "data": studens})
    except Exception as e:
        return JsonResponse({'code': 400, 'msg': "删除到数据库失败" + str(e)})


def upload(request):
    rev_file = request.FILES.get('avatar')
    if not rev_file:
        return JsonResponse({'cod': 0, 'msg': '图片不存在'})


def add_studentmodelform(request):
    # # if request.method == "GET":
    # #     form = StudentForm()
    # #     JsonResponse({"code": 200, "data": studens})
    # # 用户POST提交数据，数据校验。
    # form = StudentForm(data=request.POST)
    # print(form)
    # studen_obj = Student.objects.all().values()
    # # 转换成为list
    # studens = list(studen_obj)
    # if form.is_valid():
    #     # 如果数据合法，保存到数据库
    #     # {'name': '123', 'password': '123', 'age': 11, 'account': Decimal('0'), 'create_time': datetime.datetime(2011, 11, 11, 0, 0, tzinfo=<UTC>), 'gender': 1, 'depart': <Department: IT运维部门>}
    #     # print(form.cleaned_data)
    #     # models.UserInfo.objects.create(..)
    #     form.save()
    #
    #     return JsonResponse({"code": 200, "data": form})
    # # 校验失败（在页面上显示错误信息）
    # return JsonResponse({"code": 200, "data": form})
    form = StudentForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"code": 200, 'data': form}
        print(form)
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict))
