from rest_framework.filters import SearchFilter

class ProductSearchFilters(SearchFilter):
    search_param = 'query'