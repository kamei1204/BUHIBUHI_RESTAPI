from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, TaskListView, TaskRetrieveView, CreateUserView, PostListView, PostRetrieveView
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# viewsetと紐づける場合router.registerで関連づけることができる。
router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # <str:pk>エンドポイントの末尾に取得したいIDを日受けれるようにするためのもの
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),
    # 新規ユーザー作成のパス
    path('register/', CreateUserView.as_view(), name='register'),
    # JWT都くんを取得するためのエンドポイント　djoserがauth create JWTとゆうパスを自動的に作ってくれる
    path('auth/', include('djoser.urls.jwt')),
    # ここにきた場合routerを参照しにいってくれる
    path('', include(router.urls)),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


