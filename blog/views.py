from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html',{'posts':posts})
def reg_form(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)	
			return redirect('blog/form.html',	pk=post.pk)		
	else:
		form=PostForm()
		return render(request, 'blog/form.html',{'form':form})
def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

