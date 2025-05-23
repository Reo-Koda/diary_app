import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import PageForm
from .models import Page

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "diary/index.html")

class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "diary/page_form.html", {"form": form})

    def post(self, request):
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            return redirect("diary:index")
        return render(request, "diary/page_form.html", {"form": form})

class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.order_by("-updated_at")
        return render(request, "diary/page_list.html", {"page_list": page_list})

class PageDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "diary/page_detail.html", {"page": page})
    
class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id, author=request.user)
        form = PageForm(instance=page)
        return render(request, "diary/page_update.html", {"form": form})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id, author=request.user)
        old_picture = page.picture
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            if 'picture' in request.FILES:
                # 古い画像がある場合は削除
                if old_picture and old_picture.name != request.FILES['picture'].name:
                    old_picture_path = os.path.join(settings.MEDIA_ROOT, old_picture.name)
                    if os.path.exists(old_picture_path):
                        os.remove(old_picture_path)
            form.save()
            return redirect("diary:page_detail", id=id)
        return render(request, "diary/page_form.html", {"form": form})

class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id, author=request.user)
        return render(request, "diary/page_confirm_delete.html", {"page": page})
    
    def post(self, request, id):
        page = get_object_or_404(Page, id=id, author=request.user)
        page.delete()
        return redirect("diary:page_list")
    
class UserDetailView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "diary/user.html")



index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDetailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()
user = UserDetailView.as_view()