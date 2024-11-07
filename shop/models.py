from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام دسته')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='اسلاگ')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:products_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='دسته بندی')
    name = models.CharField(max_length=255, verbose_name='نام محصول')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ')
    description = models.TextField(max_length=3000, verbose_name='توضیحات')
    inventory = models.PositiveIntegerField(default=0, verbose_name='موجودی محصول')
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    off = models.PositiveIntegerField(default=0, verbose_name='تخفیف(%)')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت پس از تخفیف')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class ProductFeatured(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام ویژگی')
    value = models.CharField(max_length=255, verbose_name='مقدار ویژگی')
    product = models.ForeignKey(Product, related_name='features', verbose_name='محصول ها', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ":" + self.value


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='محصول')
    file = models.ImageField(upload_to="product_image/%Y/%m/%d")
    title = models.CharField(max_length=255, verbose_name='عنوان', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"
