from spotify.components.base import Component
from spotify.core.search_request import SearchRequest


class Search(Component):
    def search(self, query, query_type='tracks', start=0, count=10, callback=None):
        request = SearchRequest(
            self.sp,
            query, query_type,
            start, count
        )

        return self.request_wrapper(request, callback)
