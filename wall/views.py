from django.shortcuts import render
from django.http import Http404
from .models import WallImage, Catlog, HomePage
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


def home(request):
    # home page top image
    random_head_image = HomePage.objects.order_by('?')[:1]
    # end
    catlog_item = Catlog.objects.order_by('?')[:8]
    popular_item = Catlog.objects.order_by('?')[:7]
    latest_uploaded = WallImage.objects.order_by('?')[:30]
    images_data = WallImage.objects.order_by('-id')[:30]
    context = {
        'popular_item':popular_item,
        'catlog_item': catlog_item,
        'random_head_image': random_head_image,
        'latest_uploaded': latest_uploaded,
        'images_data': images_data,
    }
    return render(request, 'wall/index.html', context)


def images(request):
    catlog_small = Catlog.objects.order_by('?')[:18]
    catlog_items = Catlog.objects.order_by('id')[:29]
    images_data = WallImage.objects.order_by('-id')
    paginator = Paginator(images_data, 30)
    page = request.GET.get('page')
    images_data = paginator.get_page(page)
    context = {
        'catlog_items': catlog_items,
        'catlog_small': catlog_small,
        'images_data': images_data,
    }
    return render(request, 'wall/images.html', context)


def picture(request, pic_id):
    catlog_item = Catlog.objects.order_by('?')[:18]
    picture_data = WallImage.objects.get(id=pic_id)
    # remove after installing search similar items
    random_image = WallImage.objects.order_by('?')[:15]
    context = {
        'catlog_item': catlog_item,
        'picture_data': picture_data,
        'random_image': random_image
    }
    return render(request, 'wall/pic.html', context)


def catlog(request):
    catlog_item = Catlog.objects.order_by('id')
    paginator = Paginator(catlog_item, 21)
    page = request.GET.get('page')
    catlog_item = paginator.get_page(page)
    context = {
        'catlog_item': catlog_item
    }
    return render(request, 'wall/catlog.html', context)


def explore(request):
    catlog_small = Catlog.objects.order_by('?')[:18]
    catlog_items = Catlog.objects.order_by('?')[:29]
    images_data = WallImage.objects.order_by('?')
    paginator = Paginator(images_data, 30)
    page = request.GET.get('page')
    images_data = paginator.get_page(page)
    context = {
        'catlog_items': catlog_items,
        'catlog_small': catlog_small,
        'images_data': images_data,
    }
    return render(request, 'wall/explore.html', context)

def catlog_search(request, cat_item):
    catlog_small = Catlog.objects.order_by('?')[:18]
    catlog_items = Catlog.objects.order_by('id')[:29]
    template = 'wall/catlog_search.html'
    queryset_list = WallImage.objects.all()
    query = cat_item
    if query == '':
        return HttpResponseRedirect('/')
    else:
        if query:
            queryset_list = queryset_list.filter(
                Q(image_tags__icontains=query) |
                Q(image_type__icontains=query)
            ).order_by('-id')
            random_search = WallImage.objects.order_by('?')[:1]
            paginator = Paginator(queryset_list, 30)
            page = request.GET.get('page')
            result = paginator.get_page(page)
            context = {
                'catlog_items': catlog_items,
                'catlog_small': catlog_small,
                'result': result,
                'random_search': random_search,
            }
            return render(request, template, context)
        else:
            messages.error(request, 'no results found')


def search(request):
    template = 'wall/search.html'
    queryset_list = WallImage.objects.all()
    query = request.GET.get('q')
    if query == '':
        return HttpResponseRedirect('/')
    else:
        if query:
            queryset_list = queryset_list.filter(
                Q(image_type__icontains=query) |
                Q(image_tags__icontains=query)

            ).order_by('-id')
            catlog_small = Catlog.objects.order_by('?')[:18]
            catlog_items = Catlog.objects.order_by('id')[:29]
            paginator = Paginator(queryset_list, 30)
            page = request.GET.get('page')
            result = paginator.get_page(page)
            context = {
                'catlog_items': catlog_items,
                'catlog_small': catlog_small,
                'result': result,
                'catlog_items': catlog_items,
                'catlog_small': catlog_small,
                'result': result,
            }
            return render(request, template, context)
        else:
            messages.error(request, 'no results found')
