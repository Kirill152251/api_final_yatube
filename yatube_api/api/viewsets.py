from rest_framework import mixins, viewsets


class CreateGetListViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
