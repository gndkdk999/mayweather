from django.urls import path
from post.views import index, NewPost, PostDetails, tags, like, favorite,commentdelete, Map

urlpatterns = [
   	path('', index, name='index'),
    path('map/', Map, name="map"),
   	path('newpost/', NewPost, name='newpost'),
   	path('<uuid:post_id>', PostDetails, name='postdetails'),
   	path('<uuid:post_id>/like', like, name='postlike'),
   	path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
   	path('tag/<slug:tag_slug>', tags, name='tags'),
	path('commentdelete/<int:id>', commentdelete, name="commentdelete"),   
]
