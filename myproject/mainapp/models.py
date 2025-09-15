from django.db import models

# Create your models here.


class Prosthetics(models.Model):
    TYPE_PROSTHETICS_RU = (
        ('hand_prosthetics', 'Протез руки'),
        ('foot_prosthetics', 'Протез ноги')
    )
    TYPE_PROSTHETICS_UZ = (
        ('hand_prosthetics', "Protez qo'l"),
        ('foot_prosthetics', "Protez oyoq")
    )
    STATUS_PROSTHETICS = (
        ('ready', 'готов'),
        ('coming', 'скоро')
    )
    name_ru = models.CharField(
        max_length=100,
        verbose_name='Название протеза на рус'
    )
    name_uz = models.CharField(
        max_length=100,
        verbose_name='Название протеза на узб'
    )
    description_ru = models.TextField(
        max_length=600,
        verbose_name='Описание на рус'
    )
    description_uz = models.TextField(
        max_length=600,
        verbose_name='Описание на узб'
    )
    image = models.ImageField(
        upload_to='images/prosthetics/',
    )
    type_prosthetics_ru = models.CharField(
        choices=TYPE_PROSTHETICS_RU,
        max_length=100,
        verbose_name='Тип протеза на рус'
    )
    type_prosthetics_uz = models.CharField(
        choices=TYPE_PROSTHETICS_UZ,
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Тип протеза на узб'
    )
    status = models.CharField(
        choices=STATUS_PROSTHETICS,
        max_length=100,
        verbose_name='Статус протеза'
    )


    def __str__(self):
        return self.name_ru


    class Meta:
        verbose_name = 'Протез'
        verbose_name_plural = 'Протезы'


class Reviews(models.Model):
    image_review = models.ImageField(
        upload_to='images/reviews/',
        verbose_name='Картинка для отзывов'
    )
    name_review_ru = models.CharField(
        max_length=100,
        verbose_name='Имя человека для отзыва на рус'
    )
    name_review_uz = models.CharField(
        max_length=100,
        verbose_name='Имя человека для отзыва на узб'
    )
    description_review_ru = models.TextField(
        max_length=1000,
        verbose_name='Описание отзыва на рус'
    )
    description_review_uz = models.TextField(
        max_length=1000,
        verbose_name='Описание отзыва на узб'
    )


    def __str__(self):
        return self.name_review_ru


    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'


class Staff(models.Model):
    name_staff_ru = models.CharField(
        max_length=100,
        verbose_name='Имя сотрудника на рус'
    )
    name_staff_uz = models.CharField(
        max_length=100,
        verbose_name='Имя сотрудника на узб'
    )
    position_staff_ru = models.CharField(
        max_length=100,
        verbose_name='Должность сотрудника на рус'
    )
    position_staff_uz = models.CharField(
        max_length=100,
        verbose_name='Должность сотрдуника на узб'
    )
    description_staff_ru = models.TextField(
        max_length=1000,
        verbose_name='Описание на рус'
    )
    description_staff_uz = models.TextField(
        max_length=1000,
        verbose_name='Описание на узб'
    )
    image_staff = models.ImageField(
        upload_to='images/staff/',
        verbose_name='Картинка сотрудника'
    )


    def __str__(self):
        return self.name_staff_ru


    class Meta:
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'