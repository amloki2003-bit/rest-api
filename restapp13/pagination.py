from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

#working with page number pagination
# class MyPagination(PageNumberPagination):
#     page_size = 3
#     page_query_param = 'p'


# #working limit offset pagination
# class MyPagination(LimitOffsetPagination):
#     default_limit = 3()
#     max_limit = 5
#     limit_query_param = 'l'
#     offset_query_param = 'o'

#working with cursor pagination

class MyPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'c'

    
    

