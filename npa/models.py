from django.db import models

class NpaCategory(models.Model):
    name = models.CharField('Название категории', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории НПА'
        verbose_name_plural = 'Категории НПА'

class NpaDoc(models.Model):
    category = models.ForeignKey(NpaCategory, related_name='npa_category', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField('Названия документа', max_length=255)
    number = models.CharField('Номер документа', max_length=255)
    pdff = models.FileField('PDF', upload_to='pdf_file')
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Добавление НПА'
        verbose_name_plural = 'Добавление НПА'
