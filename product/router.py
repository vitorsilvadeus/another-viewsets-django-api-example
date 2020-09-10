from rest_framework import routers
from product.views import ProductViewset, KitRetrieveViewset, KitPostViewset

router = routers.DefaultRouter()
router.register(r'products', ProductViewset, basename='products')
router.register(r'retrievekits', KitRetrieveViewset, basename='retrievekits')
router.register(r'postkits', KitPostViewset, basename='postkits')
