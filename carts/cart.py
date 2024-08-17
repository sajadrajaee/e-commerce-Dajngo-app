from django.conf import settings
from products.models import NewProducts, FeaturedProducts
from decimal import Decimal
class Cart(object):
    """
    this class lets users to manage their cart
    """
    def __init__(self, request):
        self.session = request.session #this line make it accessable to other methods of class
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, product, quantity=1, override_quantity = False): #used to add item to cart
        """ 
        product: takes the product to add or edit in cart  
        quantity : quantity of product
        ov-qu: tells whether the quantity needs to be overriden(1) or new quantity must be added(0)
        
        """
        product_id = str(product.id) #we use it as key in cart's content dict
        #it is converted to str beacuase DJANGO USES JSON TO SERIALIZE SERSSION DATA and json lets str as key
        if product_id not in self.cart:
            #this doesn't let items to be added multiple times  
            self.cart[product_id] = {'quantity':0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save() #it acts like session.modified = True; that saves any time there is a new changes
        
    def remove(self, product): #used to remove item to cart
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
        
    def __iter__(self):
        """ this helps to iterate through products and access related product instances """
        product_ids = self.cart.keys()
        products = NewProducts.objects.filter(id__in= product_ids) and FeaturedProducts.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price'] * item['quantity'])
            yield item
            
    def __len__(self):
        return len([item['quantity'] for item in self.cart.values()])
    
    def get_total_price(self):
        return (Decimal(item['price'])*item['quantity'] for item in self.cart.values())
    
    def clear(self):
        for key in list(self.cart.keys()): #using list creates a copy of keys
            del self.cart[key]
        self.save()
        