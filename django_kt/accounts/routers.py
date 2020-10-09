from django_kt.accounts.viewsets import UserViewSet
from django_kt.base.routers import DjangoKtBaseRouter


accounts_router_v1 = DjangoKtBaseRouter()

accounts_router_v1.register(r'user', UserViewSet)
