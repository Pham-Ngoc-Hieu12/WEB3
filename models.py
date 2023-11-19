from django.db import models

class Coupon(models.Model):
  code = models.CharField(max_length=50, unique=True)
  discount = models.PositiveIntegerField(help_text='discount in percentage')
  active = models.BooleanField(default=True)
  active_date = models.DateField()
  expiry_date = models.DateField()
  required_amount_to_use_coupon = models.PositiveBigIntegerField()
  create_date = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.code