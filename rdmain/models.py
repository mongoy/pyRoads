from django.db import models


class TypeRoad(models.Model):
    """Типы дорог"""
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Тип дороги')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Тип дороги"
        verbose_name_plural = "Типы дорог"
        ordering = ('name',)  # сортировка


class TypeElRoad(models.Model):
    """Типы дорог"""
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Тип элемента дороги"
        verbose_name_plural = "Типы элементов дорог"
        ordering = ('name',)  # сортировка


class Material(models.Model):
    """Типы материалов"""
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ('name',)  # сортировка


class Region(models.Model):
    """Список районов"""
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        ordering = ('name',)  # сортировка


class Road(models.Model):
    """Список дорог"""
    nroad = models.CharField(max_length=500, db_index=True, verbose_name='Наименование', default='-')
    troad = models.ForeignKey(TypeRoad, on_delete=models.DO_NOTHING, verbose_name='Тип дороги', default='-')
    nregion = models.ForeignKey(Region, on_delete=models.DO_NOTHING, null=True, verbose_name='Район', default='г.Чита')
    lroad = models.FloatField(max_length=10, verbose_name='Протяженность', default=0)
    yroad = models.CharField(max_length=4, verbose_name='Год ввода', default='1970')
    inroad = models.CharField(max_length=10, null=True, verbose_name='Дата ввода')
    outroad = models.CharField(max_length=10, null=True, verbose_name='Дата снятия с учета', default='-')
    broad = models.FloatField(max_length=50, verbose_name='Балансовая стоимость')
    oroad = models.FloatField(max_length=50, verbose_name='Остаточная стоимость')
    proad = models.CharField(max_length=25, verbose_name='Пикеты', default='0+000 - 0+000')
    iroad = models.CharField(max_length=20, verbose_name='Идентификатор', default='-')
    innroad = models.CharField(max_length=20, verbose_name='Инвентарный №', default='-')
    period = models.FloatField(max_length=2, verbose_name='Период эксплуатации', default=30)
    onbal = models.BooleanField('На балансе')
    data_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nroad

    class Meta:
        verbose_name = "Дорога"
        verbose_name_plural = "Дороги"
        ordering = ('nregion', 'nroad',)  # сортировка


class ElRoad(models.Model):
    """Список элементов дорог"""
    nelroad = models.ForeignKey(TypeElRoad, on_delete=models.DO_NOTHING, verbose_name='Тип элемента дороги',
                                default='-')
    elmat = models.ForeignKey(Material, on_delete=models.DO_NOTHING, default='-')
    nroad = models.ForeignKey(Road, on_delete=models.DO_NOTHING, verbose_name='Наименование дороги', default='-')
    nregion = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name='Район', default='г.Чита')
    eldisl = models.CharField(max_length=20, verbose_name='Размещение', default='-')
    kolvo = models.FloatField(max_length=10, verbose_name='Количество', default=0)
    yroad = models.CharField(max_length=4, verbose_name='Год ввода', default='1970')
    inroad = models.CharField(max_length=10, null=True, verbose_name='Дата ввода')
    outroad = models.CharField(max_length=10, null=True, verbose_name='Дата снятия с учета', default='-')
    proad = models.CharField(max_length=25, verbose_name='Пикеты', default='0+000 - 0+000')
    prim = models.CharField(max_length=250, verbose_name='Примечание', default='-')
    onbal = models.BooleanField(verbose_name='На балансе')
    data_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nelroad.name

    class Meta:
        verbose_name = "Элемент дороги"
        verbose_name_plural = "Элементы дорог"
        ordering = ('nregion', 'nroad', 'nelroad')  # сортировка
