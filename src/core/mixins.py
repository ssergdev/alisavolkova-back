import os
from rest_framework import pagination
from rest_framework.response import Response


class DefaultPagination(pagination.LimitOffsetPagination):
    default_limit = 24


class ExtraFieldsSerializerMixin:
    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class PaginationViewMixin:
    def list(self, request):
        pagination = request.query_params.get('pagination', None)
        if pagination:
            self.pagination_class = DefaultPagination
        return super(PaginationViewMixin, self).list(request)


class MultipleSerializersMixin:
    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'retrieve_serializer_class'):
                return self.retrieve_serializer_class
            else:
                return self.serializer_class
        elif self.action in ['create', 'update', 'partial_update']:
            if hasattr(self, 'admin_serializer_class'):
                return self.admin_serializer_class
            else:
                return self.serializer_class
        else:
            return self.serializer_class
