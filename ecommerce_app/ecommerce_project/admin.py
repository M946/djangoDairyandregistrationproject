from django.contrib import admin
from .models import Product , Customer , Cart

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','Product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']


#@admin.register(Cart)
#class CartModelAdmin(admin.ModelAdmin):
    #list_display = ['id', 'user', 'product_display', 'quantity']

    #def product_display(self, obj):
        #return obj.product.title

    #product_display.short_description = 'Product Title'



