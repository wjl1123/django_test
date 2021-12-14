from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Bookmark

"""
함수형 뷰 페이지네이션
@login_required
def paging(request):
    model_list = Bookmark.objects.all()
    paginator = Paginator(model_list, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'bookmark_list.html', {'bookmark': page_obj})
"""

class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark  # need Model attr
    paginate_by = 5                    # 제너릭뷰 페이지네이션
    queryset = Bookmark.objects.all()  # 제너릭뷰 페이지네이션


class BookmarkCreateView(CreateView): # create / update 뷰들은 어떤 내용을 수정할 건지 알려주는 field가 필요하다
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
