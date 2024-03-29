import imp
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, CategoryViewSet, OrderViewSet
from store import views
from .views import MyTokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'store'

router = DefaultRouter()

router.register('customer', CustomerViewSet, basename='customer')
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')
router.register('order', OrderViewSet, basename='order')


urlpatterns = router.urls

urlpatterns += [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]












# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('', views.index, name='index')
# ]