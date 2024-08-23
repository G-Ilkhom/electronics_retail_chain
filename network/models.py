from django.db import models


class Network(models.Model):
    LEVEL = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=100, verbose_name="Название"),
    level = models.IntegerField(choices=LEVEL, verbose_name="Уровень поставщика")
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Поставщик", null=True, blank=True)
    debt_to_supplier = models.DecimalField(max_digits=20, decimal_places=2, default=0.00,
                                           verbose_name="Задолженность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    supplier = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name="Поставщик")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.supplier}"


class Product(models.Model):
    supplier = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name="Поставщик")
    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateTimeField(verbose_name="Дата выхода продукта на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.supplier}"
