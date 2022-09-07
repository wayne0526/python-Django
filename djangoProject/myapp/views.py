from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from myapp.models import register_account, Web
from django.http import HttpResponse
from selenium import webdriver
import time


# Create your views here.
# 登入前畫面
@csrf_exempt
def NewFile(request):
    return render(request, "NewFile.html")


# 註冊
@csrf_exempt
def Register(request):
    return render(request, "Register.html")


# 存進資料庫
@csrf_exempt
def login(request):
    username_list = request.POST.get('username')
    password_list = request.POST.get('password')
    email_list = request.POST.get('email')
    name_list = request.POST.get('name')
    phone_list = request.POST.get('phone')
    gender_list = request.POST.get('gender')
    birthday_list = request.POST.get('birthday')

    test = register_account(
        username_list=username_list,
        password_list=password_list,
        email_list=email_list,
        name_list=name_list,
        phone_list=phone_list,
        gender_list=gender_list,
        birthday_list=birthday_list,
    )
    test.save()
    return render(request, "NewFile.html")


# 登入判別
@csrf_exempt
def loginsuccess(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    xxx = register_account.objects.all()
    text = "<h4>管理介面</h4>"

    st = []
    sd = []
    for i in xxx:
        st.append(i.username_list)
        sd.append(i.password_list)
    if username == "wanye" and password == "123":
        return HttpResponse(text)
    else:
        if username in st and password in sd:
            return render(request, "front page.html")
        else:
            return render(request, "Login_failed.html")


# 登入失敗
@csrf_exempt
def login_failed(request):
    return render(request, "Login_failed.html")


# 登入成功畫面
@csrf_exempt
def front_page(request):
    return render(request, "front page.html")


# 爬蟲
@csrf_exempt
def newtab(request):
    blood = request.POST.get('blood')
    date1 = request.POST.get('date1')
    date2 = request.POST.get('date2')

    key1 = blood
    key2 = date1
    key3 = date2

    # driver = webdriver.Chrome(PATH)
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    # PATH = "C:/Users/USER/OneDrive/桌面/chromedriver.exe"
    # driver = webdriver.Chrome(PATH, chrome_options=option)
    driver = webdriver.Chrome(chrome_options=option)
    url = 'https://travel.liontravel.com/search?DepartureID=&ArriveID=A' + key1 + '-51-9,&GoDateStart=' + key2 + '&GoDateEnd=' + key3 + '&IsEnsureGroup=false&IsSold=true&GroupID=&Keywords=&TravelType=1'
    driver.get(url)
    driver.set_window_size(320, 568)  # 設定大小
    time.sleep(5)

    for page in range(0):
        driver.find_element_by_css_selector('div.moreInfoWrapper--3U9qW').click()
        time.sleep(11)
    title = driver.find_elements_by_css_selector('span.caption--mphmX')
    img = driver.find_elements_by_css_selector('a.cardsList--2cG2D img')
    money = driver.find_elements_by_css_selector('div.sellPrice--3fg38')
    url = driver.find_elements_by_css_selector('a.cardsList--2cG2D')
    for t, i, m, u in zip(title, img, money, url):
        test = Web(
            title = t.text,
            img=i.get_attribute('src'),
            money=m.text,
            url=u.get_attribute('href'),
        )
        test.save()
    driver.close()
    post_list = Web.objects.all()
    return render(request, 'newweb.html', {
        'post_list': post_list,
    })

@csrf_exempt
def newweb(request):
    return render(request, "newweb.html")
