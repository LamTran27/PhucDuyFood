from django.db import models
from django.utils.text import slugify

# Create your models here.
class CustomerLead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    # 🔹 Mô tả ngắn gọn cho SEO & quảng cáo
    short_description = models.CharField(max_length=300, blank=True, null=True)

    # 🔹 Mô tả chi tiết cho landing page
    full_description = models.TextField(blank=True, null=True)

    # 🔹 Giá bán (nếu có)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # 🔹 Từ khóa quảng cáo (Google Ads, Facebook Ads)
    keywords = models.CharField(max_length=255, blank=True, null=True)

    # 🔹 Meta title & meta description cho SEO
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=300, blank=True, null=True)

    # 🔹 Trạng thái hiển thị (ẩn/hiện)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='products',
    default=1  # hoặc ID của danh mục mặc định bạn muốn
    )

    # 🔹 Ngày tạo & cập nhật
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.name} ({self.code})"
    


