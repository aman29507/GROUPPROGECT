from django.shortcuts import render , get_object_or_404, redirect
from .models import Content
from .forms import ContentForm

def index(request):
    return render(request, 'content_management/index.html')

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content_management/content_list.html', {'contents': contents})

def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    return render(request, 'content_management/content_detail.html', {'content': content})

def create_content(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content_list')  # Ensure this URL is mapped in urls.py
    else:
        form = ContentForm()
    return render(request, 'content_management/content_form.html', {'form': form})



# Create your views here.
