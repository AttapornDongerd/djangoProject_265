from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def personalrecord(request):
    return render(request, 'personalrecord.html')

def education(request):
    return render(request, 'education.html')

def interests(request):
    return render(request, 'interests.html')

def product(request):
    return render(request, 'product.html')

def rolemodel(request):
    return render(request, 'rolemodel.html')

def showMyData(request):
    showID = '65342310265-8'
    showName = "อรรถพร ดอนเกิด"
    showAddress = "99 หมู่ 9 ต.เกษตรวิสัย อ.เกษตรวิสัย จ.ร้อยเอ็ด"
    showtel = "0984616825"
    showgender = "หญิง"
    showBirthday = "09 สิงหาคม 2544"
    showWeight = 52
    showHeight = 165
    showstatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product =['Spring Skirt',290.00,'../../static/images/prod1.png']
    products.append(product)
    product =['Basic Boy Jeans',289.00,'../../static/images/prod2.png']
    products.append(product)
    product =['Brownie Crop',250.00,'../../static/images/prod3.png']
    products.append(product)
    product =['Polo Neck Top',259.00,'../../static/images/prod4.png']
    products.append(product)
    product =['Longsai Shirt',290.00,'../../static/images/prod5.png']
    products.append(product)
    product = ['Yume Skirt', 250.00,'../../static/images/prod6.png']
    products.append(product)
    product = ['Short Skirt', 260.00,'../../static/images/prod7.png']
    products.append(product)
    product = [ 'New Arrival',270.00,'../../static/images/prod8.png']
    products.append(product)
    product = [ 'Crop White', 250.00,'../../static/images/prod9.png']
    products.append(product)
    product = ['Sweaatpant', 295.00,'../../static/images/prod10.png']
    products.append(product)

    context = {'showID':showID,'showName':showName,'showAddress':showAddress,'showtel':showtel,
               'showgender':showgender,'showBirthday':showBirthday,'showWeight':showWeight,'showHeight':showHeight,
               'showstatus':showstatus,'showSchool':showSchool, 'products':products}
    return render(request,'showMyData.html',context)
