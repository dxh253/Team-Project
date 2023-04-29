from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import (
    PostSerializer,
    AllPostsSerializer,
    PostVotesSerializer,
    CategorySerializer,
    CommentSerializer,
    CommentReplySerializer,
    CommentReplySerializer,
)
from .models import Category, Post, PostVotes, Comment, CommentVote, Reply, ReplyVote
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseBadRequest
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            if isinstance(obj, PostVotes):
                return obj.user_id == request.user
            return True
        return False


class PostList(generics.ListCreateAPIView):
    # ALLOWED_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # ALLOWED_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class PostVotesList(generics.ListCreateAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        user_id = self.request.query_params.get("user_id")
        # if user_id:
        #     queryset = PostVotes.objects.filter(post_id=pk, user_id=user_id)
        # else:
        #     queryset = PostVotes.objects.filter(post_id=pk)
        queryset = PostVotes.objects.filter(post_id=pk)
        return queryset

    def post(self, request, pk):
        user_id = request.data.get("user_id")
        vote_value = request.data.get("vote")
        if user_id is None or vote_value is None:
            return Response(
                {"error": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            vote = PostVotes.objects.get(user_id=user_id, post_id=pk)
            vote.vote = vote_value
            vote.save()
            serializer = PostVotesSerializer(vote)
        except PostVotes.DoesNotExist:
            data = {"user_id": user_id, "vote": vote_value, "post_id": pk}
            serializer = PostVotesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(
                    {"error": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST
                )

        return Response(serializer.data)

    def delete(self, request, pk):
        user_id = request.query_params.get("user_id")
        if user_id is None:
            return Response(
                {"error": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            vote = PostVotes.objects.get(user_id=user_id, post_id=pk)
            vote.delete()
            return Response(
                {"message": "Vote deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        except PostVotes.DoesNotExist:
            return Response(
                {"error": "Vote not found."}, status=status.HTTP_404_NOT_FOUND
            )


class PostVotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostVotes.objects.all()
    serializer_class = PostVotesSerializer
    lookup_url_kwarg = "id"
    lookup_field = "id"
    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs["pk"]
        id = self.kwargs["id"]
        return PostVotes.objects.filter(post_id=post_id, id=id)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class AllPostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # This view should return a list of all the comments for the post as determined by the post_pk portion of the URL.
        post_pk = self.kwargs["post_pk"]
        return Comment.objects.filter(post=post_pk)

    def perform_create(self, serializer):
        post = generics.get_object_or_404(Post, pk=self.kwargs["post_pk"])
        serializer.save(post=post, author=self.request.user)

    # def perform_create(self, serializer):
    #     post = generics.get_object_or_404(Post, pk=self.kwargs["post_pk"])
    #     serializer.save(post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # This view should return a single comment for the post as determined by the post_pk and pk portions of the URL.
        post_pk = self.kwargs["post_pk"]
        comment_pk = self.kwargs["pk"]
        return Comment.objects.filter(post=post_pk, pk=comment_pk)


class CommentVote(generics.UpdateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # This view should return a single comment for the post as determined by the post_pk and pk portions of the URL.
        post_pk = self.kwargs["post_pk"]
        comment_pk = self.kwargs["pk"]
        return Comment.objects.filter(post=post_pk, pk=comment_pk)

    def patch(self, request, *args, **kwargs):
        comment = self.get_object()
        vote = request.data.get("vote")

        if vote == "up":
            comment.votes += 1
        elif vote == "down":
            comment.votes -= 1
        else:
            raise ValidationError("Invalid vote value.")

        comment.save()
        serializer = self.get_serializer(comment)
        return Response(serializer.data)


class CommentDelete(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    lookup_field = "pk"

    def get_queryset(self):
        post_pk = self.kwargs["post_pk"]
        comment_pk = self.kwargs["pk"]
        reply_pk = self.kwargs.get("reply_pk")

        if reply_pk is not None:
            return Reply.objects.filter(comment_id=comment_pk, pk=reply_pk)
        else:
            return Comment.objects.filter(post_id=post_pk, pk=comment_pk)

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, author=self.request.user)
        return obj

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.author != request.user:
            raise ValidationError("You cannot delete someone else's comment.")

        return super().delete(request, *args, **kwargs)


class CommentReply(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # This view should return a single comment for the post as determined by the post_pk and pk portions of the URL.
        post_pk = self.kwargs["post_pk"]
        comment_pk = self.kwargs["pk"]
        return Comment.objects.filter(post=post_pk, pk=comment_pk)

    def perform_create(self, serializer):
        parent_comment = generics.get_object_or_404(
            Comment, pk=self.kwargs["pk"])
        serializer.save(post=parent_comment.post, parent=parent_comment)


class CommentReplyCreateView(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = CommentReplySerializer

    def perform_create(self, serializer):
        comment = generics.get_object_or_404(
            Comment, pk=self.kwargs["comment_pk"])
        parent_reply_id = self.request.data.get("parent_reply", None)
        parent_reply = None
        if parent_reply_id:
            parent_reply = generics.get_object_or_404(
                Reply, pk=parent_reply_id)
        serializer.save(
            comment=comment, user=self.request.user, parent_reply=parent_reply
        )


class CommentUpvoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_pk, comment_pk):
        return get_object_or_404(Comment, post__pk=post_pk, pk=comment_pk)

    def put(self, request, post_pk, comment_pk):
        comment = self.get_object(post_pk, comment_pk)
        comment.upvote(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentDownvoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_pk, comment_pk):
        return get_object_or_404(Comment, post__pk=post_pk, pk=comment_pk)

    def put(self, request, post_pk, comment_pk):
        comment = self.get_object(post_pk, comment_pk)
        comment.downvote(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentReplyUpvoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_pk, comment_pk, reply_pk):
        return get_object_or_404(
            Reply, pk=reply_pk, comment_id=comment_pk, comment__post_id=post_pk
        )

    def put(self, request, post_pk, comment_pk, reply_pk):
        reply = self.get_object(post_pk, comment_pk, reply_pk)
        user = request.user
        vote_type = request.data.get("vote_type")

        # Check if the user has already voted on this reply
        try:
            reply_vote = ReplyVote.objects.get(reply=reply, user=user)
        except ReplyVote.DoesNotExist:
            reply_vote = None

        if vote_type == "upvote":
            if reply_vote is None:
                reply.upvotes += 1
                reply_vote = ReplyVote.objects.create(
                    reply=reply, user=user, vote_type="up"
                )
            elif reply_vote.vote_type == "up":
                # User already upvoted, so remove the upvote
                reply.upvotes -= 1
                reply_vote.delete()
            elif reply_vote.vote_type == "down":
                # User downvoted before, now they are upvoting
                reply_vote.vote_type = "up"
                reply_vote.save()
                reply.upvotes += 1
                reply.downvotes -= 1
        elif vote_type == "downvote":
            if reply_vote is None:
                reply.downvotes += 1
                reply_vote = ReplyVote.objects.create(
                    reply=reply, user=user, vote_type="down"
                )
            elif reply_vote.vote_type == "down":
                # User already downvoted, so remove the downvote
                reply.downvotes -= 1
                reply_vote.delete()
            elif reply_vote.vote_type == "up":
                # User upvoted before, now they are downvoting
                reply_vote.vote_type = "down"
                reply_vote.save()
                reply.downvotes += 1
                reply.upvotes -= 1

        reply.save()

        return Response({"upvotes": reply.upvotes, "downvotes": reply.downvotes})


class ReplyVoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, post_pk, comment_pk, reply_pk):
        return get_object_or_404(
            Reply, pk=reply_pk, comment_id=comment_pk, comment__post_id=post_pk
        )

    def put(self, request, post_pk, comment_pk, reply_pk):
        reply = self.get_object(post_pk, comment_pk, reply_pk)
        user = request.user
        vote_type = request.data.get("vote_type")

        # Check if the user has already voted on this reply
        try:
            reply_vote = ReplyVote.objects.get(reply=reply, user=user)
        except ReplyVote.DoesNotExist:
            reply_vote = None

        if vote_type == "upvote":
            if reply_vote is None:
                reply.upvotes += 1
                reply_vote = ReplyVote.objects.create(
                    reply=reply, user=user, vote_type="up"
                )
            elif reply_vote.vote_type == "up":
                # User already upvoted, so remove the upvote
                reply.upvotes -= 1
                reply_vote.delete()
            elif reply_vote.vote_type == "down":
                # User downvoted before, now they are upvoting
                reply_vote.vote_type = "up"
                reply_vote.save()
                reply.upvotes += 1
                reply.downvotes -= 1
        elif vote_type == "downvote":
            if reply_vote is None:
                reply.downvotes += 1
                reply_vote = ReplyVote.objects.create(
                    reply=reply, user=user, vote_type="down"
                )
            elif reply_vote.vote_type == "down":
                # User already downvoted, so remove the downvote
                reply.downvotes -= 1
                reply_vote.delete()
            elif reply_vote.vote_type == "up":
                # User upvoted before, now they are downvoting
                reply_vote.vote_type = "down"
                reply_vote.save()
                reply.downvotes += 1
                reply.upvotes -= 1

        reply.save()

        return Response({"upvotes": reply.upvotes, "downvotes": reply.downvotes})
