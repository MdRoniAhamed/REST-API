from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'id'