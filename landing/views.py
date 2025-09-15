from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomerLeadForm
from django.core.mail import send_mail
from .models import Product, Category
from django.db.models import Count
from django.conf import settings

# Create your views here.
def product_intro(request):
    featured_products = Product.objects.filter(is_active=True)[:5]
    all_products = Product.objects.filter(is_active=True)
    categories = Category.objects.annotate(product_count=Count('products')).filter(product_count__gt=0)
    if request.method == 'POST':
        form = CustomerLeadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # Lưu vào database
            form.save()
            # Gửi email thông báo
            send_mail(
                subject='Khách hàng mới đăng ký',
                message=f"{form.cleaned_data['name']} - {form.cleaned_data['email']} - {form.cleaned_data['phone']}",
                from_email='your_email@gmail.com',
                recipient_list=['your_email@gmail.com'],
            )

            return redirect('thank_you')
    else:
        form = CustomerLeadForm()
    return render(request, 'landing/product_intro.html', {
        'form': form,
        'featured_products': featured_products,
        'all_products': all_products,
        'categories': categories
    })

from django.core.mail import send_mail

def footer_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Gửi email đến admin
            send_mail(
                subject='Khách hàng đăng ký tư vấn',
                message=f'Email khách hàng: {email}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=settings.ADMIN_EMAILS,
                fail_silently=False,
            )

             # Gửi email xác nhận cho khách hàng
            send_mail(
                subject='PhucDuyFood - Đăng ký thành công',
                message='Cảm ơn bạn đã đăng ký nhận tư vấn từ PhucDuyFood!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            # Có thể redirect hoặc hiển thị thông báo
            return redirect('thank_you')

    return render(request, 'landing/footer.html')

def thank_you(request):
    return render(request, 'landing/thank_you.html')




