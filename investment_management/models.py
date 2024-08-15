from django.db import models

from django.db import models

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

class FinancialData(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    year = models.DateField()
    metric_type = models.CharField(max_length=50)
    metric_value = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'financial_data'
        unique_together = ('stock', 'symbol', 'year', 'metric_type')
        verbose_name = 'Financial Data'
        verbose_name_plural = 'Financial Data'

    def __str__(self):
        return f"{self.symbol} - {self.year} - {self.metric_type}"


    class FinancialData(models.Model):
        stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
        symbol = models.CharField(max_length=10)
        year = models.DateField()
        metric_type = models.CharField(max_length=50)
        metric_value = models.FloatField(null=True, blank=True)

        class Meta:
            unique_together = ('stock', 'symbol', 'year', 'metric_type')


class CompanyOfficer(models.Model):
    id = models.AutoField(primary_key=True)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    year_born = models.IntegerField(null=True, blank=True)
    exercised_value = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    unexercised_value = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    total_pay = models.IntegerField(null=True, blank=True)
    fiscal_year = models.IntegerField(null=True, blank=True)
    max_age = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'company_officer'
        constraints = [
            models.CheckConstraint(check=models.Q(id__gte=0), name='company_officer_id_gte_0')
        ]

    def __str__(self):
        return self.name
    


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    email_id = models.EmailField(max_length=255)
    message = models.TextField()
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'message'  # Ensure this matches your actual table name in the database
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        constraints = [
            models.CheckConstraint(check=models.Q(email_id__isnull=False), name='email_id_not_null')
        ]

    def __str__(self):
        return f"Message from {self.email_id} at {self.created_time}"
