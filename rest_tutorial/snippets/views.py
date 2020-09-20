from django.shortcuts import render
from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import *

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers


class SnippetViewSet(viewsets.ModelViewSet): 
	# queryset = Snippet.objects.all()
	queryset = Snippet.objects.filter(id=2)

	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializers): 
		serializer.save(owner=self.request.user)

	def get_queryset(self): 
		# queryset = Snippet.objects.all()
		#queryset = self.queryset
		# query_set = queryset.filter(id=2)
		query_set = Snippet.objects.filter(id=3)
		return query_set


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer





