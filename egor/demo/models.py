from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


class Product(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    photo_file = models.ImageField(max_length=254, upload_to=get_name_file,
                                   blank=True, null=True,
                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    year = models.IntegerField(verbose_name='Год производства', blank=True)
    country = models.CharField(max_length=254, verbose_name='Страна производства', blank=True)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, blank=False,
                                default=0.00)
    count = models.IntegerField(verbose_name='Количество', blank=False, default=0)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='Наименование', blank=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    count = models.IntegerField(verbose_name='Кол-во', blank=False, default=1)
    product = models.ForeignKey('Product', verbose_name='Продукт', on_delete=models.CASCADE)
    user = models.ForeignKey('User', verbose_name='Айди', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + " " + str(self.count)

class Order(models.Model):
        date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
        status = models.CharField(max_length=254, verbose_name='Роль',
                                choices=(('new', 'Новые'), ('confirmet', 'Подтвержденные'), ('canceled', 'Отмененные')), default='new')
        rejection_reason = models.TextField(verbose_name='Причина отказа' , blank=True)
        user = models.ForeignKey('User', verbose_name='Айди', on_delete=models.CASCADE)
        products = models.ManyToManyField('Product', through='ItemInOrder', related_name='orders')

        def __str__(self):
            return f"{self.date} - {self.user}- {str(self.products.count())}"


class ItemInOrder(models.Model):
    count = models.IntegerField(verbose_name='Кол-во', blank=False, default=0)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, blank=False, default=0.00)
    order = models.ForeignKey('Order', verbose_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name='Товар', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order.user} - {self.product.name} - {str(self.count)} - {self.product.price*self.count}"
