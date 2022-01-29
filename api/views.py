from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer, TaskSerializer
from .models import Task, Post

# 新規ユーザー登録（POST）
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # デフォルトの認証方式が適用されるため、認証が必要だが、まだユーザーが存在しないため、AllowAnyで通れるようにした
    permission_classes = (AllowAny,)
# 一覧（GET）してquerysetにset
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
# 一覧（GET）してquerysetにsetしたのを取り出す 詳細（GET）
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)
# ModelViewSetを利用すると、ひとつのクラスで（エンドポイントの切り替えて）CRUDの動き全てに対応できます。
# crudとはCreate（登録）、Read（参照）、Update（更新）、Delete（削除）機能をまとめた表現
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer




