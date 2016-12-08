from django.shortcuts import render, get_object_or_404
from .models import Page


def page_view(request, page_number):
    page = get_object_or_404(Page, index=page_number)

    return render(request, 'page.html',
                  {
                      'page': page,
                      'page_index': page.index,
                      'img_url': page.image_file.url,
                      'next_page': page.next_page
                  })
