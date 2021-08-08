""" 
|--------------------------------|
| Alexandr Drachenin | Blackgard |
|--------------------------------|

Start testing you connection to dkc api. How start you need create .env file and write master_key to "TOKEN" field. 
Check file .env.example.

Good use!

"""
import os
import loguru 

from datetime import datetime

from dkc_api.v1.dkc_api import DkcAPI
from dkc_api.v1 import storage

from dkc_api.v1.models.error import ResponceError, ResponceErrorAlternative

from dkc_api.v1.objects.catalog.models import GetMaterial, GetMaterialAccessories, GetMaterialAnalogs, GetMaterialCertificates, \
    GetMaterialDescription, GetMaterialDrawingsSketch, GetMaterialRelated, GetMaterialSpecification, GetMaterialStock, \
    GetMaterialVideo

from dkc_api.v1.objects.content.models import GetFile, GetRevisionMaterials, GetRevisionLastSize, GetRevisionCertificates, \
    GetRevisionDrawings, GetRevisionLast, PostFile, PostFileContent

from dkc_api.v1.objects.delivery.models import DeliveryTimeContent, GetDeliveryTime

from dkc_api.v1.objects.news.models import GetNewsCommunity, GetNewsCompany, GetNewsProducts

from dotenv import load_dotenv
load_dotenv()


def print_result(obj, SuccessClass):
    if isinstance(obj, SuccessClass):
        print(obj)
    elif isinstance(obj, ResponceError):
        print(f"| {obj.code} | Message: {obj.message}")
    elif isinstance(obj, ResponceErrorAlternative):
        print(f"| {obj.errorCode} | Message: {obj.errorMessage}")

def main():
    logger = loguru.logger
    
    dkc_api = DkcAPI(
        master_key=os.getenv('TOKEN'),
        debug=True,
        storage=storage.FileTokenStorage(),
        logger=logger
    )

    # Get all products on stock
    resolve = dkc_api.Catalog.getMaterialStock()
    print_result(resolve, GetMaterialStock)
    
    # Get only product with code "1" on stock
    resolve = dkc_api.Catalog.getMaterialStock(code=1)
    print_result(resolve, GetMaterialStock)

    # Get all data about a product by its code
    resolve = dkc_api.Catalog.getMaterial(code=1200)
    print_result(resolve, GetMaterial)

    # Get product analogues by code
    resolve = dkc_api.Catalog.getMaterialAnalogs(code=1200)
    print_result(resolve, GetMaterialAnalogs)

    # Get all product analogues
    resolve = dkc_api.Catalog.getMaterialAnalogs()
    print_result(resolve, GetMaterialAnalogs)
    
    # Get product accessories by code 
    resolve = dkc_api.Catalog.getMaterialAccessories(code=1200)
    print_result(resolve, GetMaterialAccessories)
    
    # Get all product accessories 
    resolve = dkc_api.Catalog.getMaterialAccessories()
    print_result(resolve, GetMaterialAccessories)
    
    # Get product certificates by code 
    resolve = dkc_api.Catalog.getMaterialCertificates(code=1200)
    print_result(resolve, GetMaterialCertificates)


    # Other object you can use by the same method


    # Get all revision drawings products
    resolve = dkc_api.Content.getRevisionDrawings()
    print_result(resolve, GetRevisionDrawings)
    
    # Get revision materials for this days
    resolve = dkc_api.Content.getRevisionMaterials(last_updated=datetime.now())
    print_result(resolve, GetRevisionMaterials)
    
    # Post file to dkc api
    post_file_content = PostFileContent(name="test", value="test file")
    resolve = dkc_api.Content.postFile(file_content=post_file_content)
    print_result(resolve, PostFile)
    
    # Get news products ( page = 1, items = 10)
    resolve = dkc_api.News.getNewsProducts()
    print_result(resolve, GetNewsProducts)
    
    # Get news company ( page = 2, items = 30)
    resolve = dkc_api.News.getNewsCompany(page_index=2, length=30)
    print_result(resolve, GetNewsCompany)

    # Get delivery time content by the items and warehouse.
    delivery_time_content = DeliveryTimeContent(company_warehouse="test", items=[])
    resolve = dkc_api.Delivery.getDeliveryTime(delivery_time_content=delivery_time_content)
    print_result(resolve, GetDeliveryTime)

if __name__ == "__main__":
    main()