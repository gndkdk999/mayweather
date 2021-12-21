from django.shortcuts import render

def newreply(request):
    if request.method == "POST":
        comment = Comment()
        comment.comment_body = request.POST['comment_body']
        comment.blog = Blog.objects.get(pk=request.POST['blog'])
        author = request.POST['user']
        print(type(author2), author2)
        if author:
            comment.comment_user = User.objects.get(username=author)
        else:
            return redirect('blog:detail', comment.blog.id)
        comment.comment_date = timezone.now()
        comment.save()

        return redirect('blog:detail', comment.blog.id)
    else:
        return redirect('home')
        
# Create your views here.
