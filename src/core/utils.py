from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings


class HTMLCustomPaginator(Paginator):
    def __init__(self, *args, **kwargs):
        """
        :param wing_pages: How many pages will be shown before and after current page.
        """
        self.wing_pages = kwargs.pop('wing_pages', settings.NUMBER_OF_WING_PAGES)
        super().__init__(*args, **kwargs)

    def _get_page(self, *args, **kwargs):
        self.page = super(HTMLCustomPaginator, self)._get_page(*args, **kwargs)
        return self.page

    @property
    def page_range(self):
        return range(max(self.page.number - self.wing_pages, 1),
                     min(self.page.number + self.wing_pages + 1, self.num_pages + 1))

    @property
    def extra_page(self):
        return self.page_range[-1] + 1


def create_pagination(request, qs):
    page = request.GET.get('page', 1)
    paginator = HTMLCustomPaginator(qs, settings.NUMBER_OF_ELEMENTS_PER_PAGE)
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)
    return qs


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def slice_into_columns(news_lst, num_columns=4):
    counter = 0
    columns = [[] for _ in range(num_columns)]
    for el in news_lst:
        if counter == num_columns:
            counter = 0
        columns[counter].append(el)
        counter += 1
    return columns