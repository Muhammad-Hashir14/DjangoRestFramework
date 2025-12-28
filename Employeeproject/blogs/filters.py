import django_filters
from .models import Blogs

class BlogsFilters(django_filters.FilterSet):
    
    title_filter = django_filters.CharFilter(field_name="blog_title", lookup_expr="icontains") # iexact
    blog_id = django_filters.RangeFilter(field_name="id")


    class Meta:
        model = Blogs
        fields = ['title_filter', 'blog_id']
        