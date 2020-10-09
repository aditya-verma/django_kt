from rest_framework import routers


class DjangoKtBaseRouter(routers.SimpleRouter):
    def extend(self, extended_router=None):
        if extended_router:
            self.registry.extend(extended_router.registry)
