from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    product_desc = models.CharField(max_length=300, default='')
    product_price = models.IntegerField(default=0)
    product_pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
