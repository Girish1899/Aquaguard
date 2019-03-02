from django.views.decorators.csrf import csrf_exempt

from .models import Product
from .views import success,fail


@csrf_exempt
def createNewDevice(request):
    if request.method=="POST":
        name=request.POST.get("name", None)
        year=request.POST.get("year", None)
        product_id=request.POST.get("product_id", None)
        cost=request.POST.get("cost", None)
        description=request.POST.get("description", None)
        category=request.POST.get("category", None)
        feature=request.POST.get("feature", None)
        if (not(name==None and year==None and product_id==None and cost==None and description==None and category==None and feature==None)):
            print (name)
            print(year)
            print(category)
            print("thats all")
            try:
                newProduct=Product(name=name,year=year,product_id=product_id,cost=cost,description=description,category=category,features=feature)
                newProduct.save()
                print(newProduct.id)
                return success("new product saved")

            except:
                return fail("Product id already exists")

        else:
            return fail("Invalid credentials")

    return fail("something went wrong")


@csrf_exempt
def displayAllDevice(request):
    products=Product.objects.all()
    out=[]
    for i in range(len(products)):
        pro=products[i]
        product={}
        product['id']=pro.id;
        product['name']=pro.name
        product['year']=pro.year
        product['product_id']=pro.product_id
        product['cost']=pro.cost
        product['description']=pro.description
        product['feature']=pro.features
        product['category']=pro.category
        out.append(product)

    return success(out)


@csrf_exempt
def deleteDevice(request):
    if request.method=="POST":
        product_id=request.POST.get("product_id",None)
        if(not(product_id==None)):
            try:
                product=Product.objects.get(product_id=product_id)
                product.delete()
                return success("Item deleted")
            except:
                return fail("Product id does not exist")
        else:
            return fail("fail")

#Returns the data related to a specific product
#input param: pid
@csrf_exempt
def getProductDetails(request):
    if request.method=="POST":
        product_id=request.POST.get("pid",None)
        if(not(product_id==None)):
            try:
                pro=Product.objects.get(product_id=product_id)
                data={}
                data['name']=pro.name
                data['year']=pro.year
                data['product_id']=pro.product_id
                data['cost']=pro.cost
                data['description']=pro.description
                data['feature']=pro.features
                data['category']=pro.category

                return success(data)
            except:
                return fail("Product id does not exist")
        else:
            return fail("fail")



