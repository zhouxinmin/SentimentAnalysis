# coding:utf-8
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from senan import test3
from django.http import HttpResponse
# from senan.models import *

# Create your views here.


def senan(request):
    """
    主界面
    :param request:
    :return:
    """
    return render(request, 'main.html')


class UserForm(forms.Form):
    """
    用户登陆表单
    """
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


def login(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect(reverse('senan:mainsys'))
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect(reverse('senan:login'))
    else:
        uf = UserForm()
    return render(request, 'index.html', {'uf': uf})


def logout(request):
    """

    :param request:
    :return:
    """
    return


def importBasicData(request):
    """
    导入基础数据View
    :param request:
    :return:
    """
    # if request.method == 'POST':
    #     form = basicDataForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         res = importData.importCSVData(request.FILES['filename'], request.POST['dbName'])
    #         return render(request, 'importBasicDataRes.html', {'res':res})
    #     else:
    #         print form.errors
    # else:
    #     form = basicDataForm()
    return render(request, 'importBasicData.html')


def basicdataview(request):
    """
        导入基础数据View
        :param request:
        :return:
    """
    return render(request, 'basicDataView.html')


def assess(request):
    """
        导入基础数据View
        :param request:
        :return:
    """
    if request.method == "POST":
        qes = assessForm(request.POST)
        if qes.is_valid():
            sen = qes.cleaned_data['content']
            sentence = str(sen)
            res = test3.script_run(sentence)
            return render(request, 'index2.html', {'res': res})
        else:
            print "Failed!"
    form = assessForm()
    return render(request, 'assess.html', {'form': form})


def devdebug(request):
    """
        导入基础数据View
        :param request:
        :return:
    """
    return render(request, 'devdebug.html')


def test(request):
    """
    测试网页
    :param request:
    :return:
    """
    if request.method == "POST":
        req = testForm(request.POST)
        if req.is_valid():
            sentence = req.cleaned_data['content']

            print req.cleaned_data['content']
            print type(req.cleaned_data['content']), type(request.POST['content'])
        else:
            print "Failed!"
    form = testForm()
    return render(request, 'index2.html', {'form': form})

# ======== 表单区域


class testForm(forms.Form):
    choiceArray = (
        ('caveinfo', '热压罐'),
        ('caveStopPlan', '热压罐停工计划'),
        ('teamInfo', '铺叠工作组'),
        ('teamStopPlan', '铺叠工作组停工计划'),
        ('teamWorkPlan', '铺叠工作组倒班计划'),
        ('toolsInfo', '工装表'),
        ('toolsFixPlan', '工装维护计划'),
        ('basicData', '基础数据'),
        ('componentInfo', '零件'),
        ('componentSuggest', '零件建议'),
        ('processInfo', '工艺流程'),
        ('materialInfo', '原材料'),
        ('componentMaterialNeed', '零件材料需求'),
        ('fixedPackage', '固定包'),
        ('inOnePackage', '多件共袋'),
        ('order', '订单'),
        ('extreOrder', '插单'),
    )
    dbName = forms.ChoiceField(choices=choiceArray, label="数据库名称")
    inputName = forms.CharField(label="测试输入")
    timeTest = forms.DateField(label="时间输入")


class assessForm(forms.Form):
    choiceArray = (
        ('national_level', '国家级'),
        ('provincial_and_ministerial_level', '省部级'),
        ('Bureau_level', '厅局级'),
    )
    level = forms.ChoiceField(choices=choiceArray, label="课题级别")
    money = forms.IntegerField(label="资助金额(万)")
    title = forms.CharField(label="标题:")
    content = forms.CharField(label="内容:")