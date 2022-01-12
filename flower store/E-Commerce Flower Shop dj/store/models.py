from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    created_at = models.DateTimeField( auto_now_add=True)
    slug = models.SlugField(blank=True , null=True)
    favorite = models.ManyToManyField(User, related_name="favorite" ,  blank=True)
    quantity = models.IntegerField(default=1)
   
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        # ordering 
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            return super(Item , self).save(*args, **kwargs)

    # for product details 
    def get_absolute_url(self):
        return reverse("store:flower_details", kwargs={"id": self.id})

    # for add to cart 

    def get_add_to_cart_url(self):
        return reverse("store:add_to_cart", kwargs={"slug": self.slug})


    def get_remove_from_cart_url(self):
        return reverse("store:remove_from_cart", kwargs={"slug": self.slug})
    


    

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True , null=True)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _("OrderItem")
        verbose_name_plural = _("OrderItems")

    def __str__(self):
        return str(self.item.name)




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.user.username




