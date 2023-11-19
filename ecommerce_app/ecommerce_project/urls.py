
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm, MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.ecommerce_project, name='ecommerce_project'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>/', views.CategoryView.as_view(), name="category"),
    path('product-details/<int:pk>/', views.ProductDetails.as_view(), name="product-details"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', views.address, name="address"),
    path('updateAddress/<int:pk>/', views.ProductDetails.as_view(), name="updateAddress"),

    #path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    #path('cart/', views.show_cart, name='show_cart'),

    # Login Authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="template/login.html", authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name="template/changepassword.html", form_class=MyPasswordResetForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='template/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="template/password_reset.html", form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name="template/password_reset_done.html", form_class=MyPasswordResetForm), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="template/password_reset_confirm.html", form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="template/password_reset_complete.html"), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
