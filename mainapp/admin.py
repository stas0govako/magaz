from PIL import Image
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PlushToyAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px;">Загружайте изображения с минимальным разрешением {}x{}</span>'.format(
              *Product.MIN_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер загружаемого изображения не должен превышать 3 МБ !!!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображение изображение  меньше минимального!!!')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Разрешение изображение изображение  больше максимального!!!')
        return image


# Вернуться к проверке разрешения

class PlasticToyAdminForm(ModelForm):
    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображения с минимальным разрешением {}x{}'.format(
            *self.MIN_RESOLUTION
        )


class AntistressToyAdminForm(ModelForm):
    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображения с минимальным разрешением {}x{}'.format(
            *self.MIN_RESOLUTION
        )


class PlushToyAdmin(admin.ModelAdmin):

    form = PlushToyAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='plushtoys'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PlasticToyAdmin(admin.ModelAdmin):

    form = PlasticToyAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='plastictoys'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AntisressToyAdmin(admin.ModelAdmin):

    form = AntistressToyAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='antisresstoys'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(PlushToy, PlushToyAdmin)
admin.site.register(PlasticToy, PlasticToyAdmin)
admin.site.register(AntistressToy, AntisressToyAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
