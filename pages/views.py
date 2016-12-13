from django.shortcuts import render, get_object_or_404

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .models import Page


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('next_page', 'index', 'image_file', 'click_count', 'limit')


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    # ReadOnlyModelViewSet

    def retrieve(self, request, pk=None):
        return page_view(request, pk)


    @detail_route(methods=['post'])
    def send_click(self, request, pk=None):
        page = self.get_object()

        result = page.click()
        if result:
            print "exceeded"
        else:
            print "clicked: " + str(page.click_count)
            page.save(update_fields=["click_count"])

        return Response({
            'status': status.HTTP_202_ACCEPTED,
            'result': result,
            'count': page.click_count,
            'limit': page.limit
        })


def page_view(request, page_id):
    page = get_object_or_404(Page, pk=page_id)

    return render(request, 'page.html',
                  {
                      'page': page,
                      'page_index': page.index,
                      'img_url': page.image_file.url,
                      'next_page': page.next_page
                  })
