from django.db import models


class Profcom(models.Model):
    text = models.CharField('Текст', max_length=255)
    date = models.DateField('Дата публикации')
    full_text = models.TextField('Описание', null=True)
    image1 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image2 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image3 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image4 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image5 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image6 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image7 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image8 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)
    image9 = models.ImageField('Фото', upload_to='profcom_file', blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Добавление мероприятий'
        verbose_name_plural = 'Добавление мероприятий'

class ProfOpros(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Добавления опросника'
        verbose_name_plural = 'Добавления опросника'

class Golos(models.Model):
    opros = models.ForeignKey(ProfOpros, on_delete=models.CASCADE, verbose_name="Опрос")
    otvet = models.CharField('Голосы', max_length=10)
    mac = models.CharField('Мак адрес',max_length=30)

    def __str__(self):
        return self.mac

    class Meta:
        verbose_name = 'Результаты годосований'
        verbose_name_plural = 'Результаты голосований'

class ListReclama(models.Model):
    name = models.CharField('Называние', max_length=250)
    url = models.CharField('Путь', max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Анонсы(не лезьте)'
        verbose_name_plural = 'Анонсы(не лезьте)'

class Reclama(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    date = models.DateField('Дата публикации')
    category = models.ForeignKey(ListReclama, on_delete=models.CASCADE)
    img = models.ImageField('Фото', upload_to='reclama_file')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Добавление обьявлений'
        verbose_name_plural = 'Добавление обьявлений'