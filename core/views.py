from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NoteForm
from .models import Note


def home_view(request):
    """Контроллер главной страницы"""
    if request.method == "GET":
        return render(request, "home.html")


@login_required
def notes_list_view(request):
    """Контроллер списка записок пользователя"""
    if request.method == "GET":
        user = request.user
        notes = user.notes.all().prefetch_related('tags')

        if "search" in request.GET:
            search_string = request.GET["search"]
            query = Q(title__icontains=search_string) | Q(text__icontains=search_string)
            notes = notes.filter(query)

        if "ordering" in request.GET:
            ordering_string = request.GET["ordering"]
            orderings = {
                "title": "title",
                "oldest": "created_at",
                "newest": "-created_at"
            }
            try:
                notes = notes.order_by(orderings[ordering_string])
            except KeyError:
                pass

        p = Paginator(notes, 2)
        try:
            page_num = int(request.GET["page"])
        except (ValueError, KeyError):
            page_num = 1
        notes = p.page(page_num).object_list

        return render(request, "notes_list.html", {"notes": notes, "page": p.page(page_num)})


@login_required
def notes_detail_view(request, pk):
    """Контроллер детализированного представления записки"""
    if request.method == "GET":
        note = get_object_or_404(Note, pk=pk)

        if note.user != request.user:
            return redirect("home")

        return render(request, "notes_detail.html", {"note": note})


@login_required
def notes_add_view(request):
    """Контроллер создания записки"""
    if request.method == "GET":
        form = NoteForm()
        return render(request, "notes_add.html", {"form": form})

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем форму без коммита, так как нужно еще прописать юзера
            note = form.save(commit=False)

            # Прописываем юзера к записке и сохраняем
            note.user = request.user
            note.save()

            # Когда сохранялась форма, не были сохранены теги, так как это m2m, который может сохраниться только после
            # создания записи в базе данных, поэтому после создания сохраняем теги через форму с помощью save_m2m
            form.save_m2m()

            return redirect("note", pk=note.pk)
        else:
            messages.error(request, "Введенные данные имели неверный формат!")
            return render(request, "notes_add.html", {"form": form})


@login_required
def notes_update_view(request, pk):
    """Контроллер изменения записки"""
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        return redirect("home")

    if request.method == "GET":
        form = NoteForm(instance=note)
        return render(request, "notes_update.html", {"form": form, "note": note})

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect("note", pk=note.pk)
        else:
            messages.error(request, "Введенные данные имели неверный формат!")
            return render(request, "notes_add.html", {"form": form, "note": note})


@login_required
def notes_delete_view(request, pk):
    """Контроллер удаления записки"""
    note = get_object_or_404(Note, pk=pk)
    if note.user != request.user:
        return redirect("home")

    if request.method == "GET":
        return render(request, "notes_confirm_delete.html", {"note": note})

    if request.method == "POST":
        note.delete()
        messages.success(request, "Записка успешно удалена!")
        return redirect("notes")
