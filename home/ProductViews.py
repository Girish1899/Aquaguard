from django.views.decorators.csrf import csrf_exempt

from .models import Product
from .views import success,fail


@csrf_exempt
def addNewProduct(request):
    if request.method=="POST":
        name=request.POST.get("name", None)
        builtYear=request.POST.get("builtYear", None)
        cost=request.POST.get("cost", None)
        description=request.POST.get("description", None)
        category=request.POST.get("category", None)
        if (not(name==None and builtYear==None and cost==None and description==None and category==None)):
            try:
                newProduct = Product(name=name, builtYear=builtYear, cost=cost, description=description, category=category)
                newProduct.save()
                return success("Product has been created")

            except Exception as e:
                print(e)
                return fail("Something went wrong")
        else:
            return fail("Invalid data")

    return fail("Error in request")


@csrf_exempt
def getAllProducts(request):
    if request.method=="POST":
        products = Product.objects.all()
        out=[]
        for i in range(len(products)):
            productObj = products[i]
            product = {}
            product['id'] = productObj.id;
            product['name'] = productObj.name
            product['builtYear'] = productObj.year
            product['cost'] = productObj.cost
            product['description'] = productObj.description
            product['category'] = productObj.category
            out.append(product)
        return success(out)
    return fail("Error in request")


@csrf_exempt
def deleteDevice(request):
    if request.method=="POST":
        product_id=request.POST.get("product_id",None)
        if(not(product_id==None)):
            try:
                product=Product.objects.get(id=product_id)
                product.delete()
                return success("Item deleted")
            except:
                return fail("Product id does not exist")
        else:
            return fail("Product is not present")
    return fail("Error in request")

#Returns the data related to a specific product
#input param: pid
@csrf_exempt
def getSingleProduct(request):
    if request.method=="POST":
        product_id=request.POST.get("pid",None)
        if(not(product_id==None)):
            try:
                productObj=Product.objects.get(id=product_id)
                data={}
                data['name']=productObj.name
                data['buitlYear']=productObj.builtYear
                data['cost']=productObj.cost
                data['description']=productObj.description
                data['category']=productObj.category

                return success(data)
            except:
                return fail("Product id does not exist")
        else:
            return fail("Product doesn't exist")
    return fail("Error in request")


@csrf_exempt
def updateProduct(request):
    if request.method=="POST":
        prod_id = request.POST.get("pid", None)
        name = request.POST.get("name", None)
        description = request.POST.get("description", None)
        builtYear = request.POST.get("builtYear", None)
        cost = request.POST.get("cost", None)
        category = request.POST.get("category", None)
        
        if id == None or id == '':
            return fail("Provide employee id")
        
        if(not(name==None and description==None and builtYear==None and cost==None and category==None)):
            try:
                prodObj = Product.objects.get(id=prod_id)
            except Exception as e:
                return fail("Product doesn't exist")
            if name is not None:
                prodObj.name = name            
            if description is not None:
                prodObj.description = description            
            if builtYear is not None:
                prodObj.builtYear = builtYear            
            if cost is not None:
                prodObj.cost = cost            
            if category is not None:
                prodObj.category = category            
            
            return success("Product successfully updated")
    return fail("Error in request")



