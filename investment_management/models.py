from django.db import models

# Create your models here.
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    exchange = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    sector_key = models.CharField(max_length=100, blank=True, null=True)
    sector_display = models.CharField(max_length=250, blank=True, null=True)
    industry_key = models.CharField(max_length=100, blank=True, null=True)
    industry_display = models.CharField(max_length=250, blank=True, null=True)
    fulltime_employees = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'stock'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return self.symbol