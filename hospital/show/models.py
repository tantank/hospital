from django.db import models

# Create your models here.
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"

class Hospital강원(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital강원"

class Hospital경기(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital경기"

class Hospital경남(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital경남"

class Hospital경북(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital경북"

class Hospital광주(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital광주"

class Hospital대구(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital대구"

class Hospital대전(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital대전"

class Hospital부산(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital부산"

class Hospital서울(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital서울"

class Hospital세종시(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital세종시"

class Hospital울산(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital울산"

class Hospital인천(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital인천"

class Hospital전남(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital전남"

class Hospital전북(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital전북"

class Hospital충남(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital충남"

class Hospital충북(models.Model):
    sidocdnm = models.CharField(max_length=8)
    sggucdnm = models.CharField(max_length=8)
    yadmnm = models.CharField(max_length=15)
    clcdnm = models.CharField(max_length=6)
    npaykornm = models.CharField(max_length=25)
    maxprc = models.IntegerField()
    minprc = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.npaykornm

    class Meta:
        verbose_name_plural = "Hospital충북"