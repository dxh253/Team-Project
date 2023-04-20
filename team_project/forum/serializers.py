from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Category, Post, PostVotes, Category, Comment, CommentVote, Reply
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    get_image = serializers.ImageField(max_length=None, use_url=True, required=False)
    isBlurred = serializers.BooleanField(default=False)  # set default value to False

    class Meta:
        model = Post
        fields = ["id","created","modified",'time_since_post',"title","description","description_br","owner",'score',"username","owner_url","category","category_name",'slug','category_slug','full_url','user_vote','get_image','isBlurred',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:posts", "lookup_field": "title"}
        }

    def create(self, validated_data):
        owner = validated_data.pop('owner', None)
        image = validated_data.pop('get_image', None)
        if owner:
            validated_data['owner_id'] = owner.pk
        if image:
            validated_data['image'] = image
        return super().create(validated_data)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image and instance.image.storage.exists(instance.image.name):
            representation['get_image'] = instance.image.url
        return representation


class PostVotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVotes
        fields = ['post_id', 'user_id', 'vote', 'id']

    def validate(self, data):
        post_id = data.get('post_id')
        user_id = data.get('user_id')
        vote = data.get('vote')

        # Check if the user has already voted for the post
        if PostVotes.objects.filter(post_id=post_id, user_id=user_id).exists():
            # If the user has already voted, allow them to change their vote
            post_vote = PostVotes.objects.get(post_id=post_id, user_id=user_id)
            if vote == post_vote.vote:
                return data

        # Check if the vote is valid
        if vote not in [choice[0] for choice in PostVotes.VOTE_CHOICES]:
            raise serializers.ValidationError('Invalid vote')

        return data

class AllPostsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    queryset = Post.objects.all()

    class Meta:
        model = Post
        fields = ["id","created","modified",'time_since_post',"title","description","description_br","owner","username","owner_url","category","category_name",'slug','category_slug','score','full_url','user_vote','user_up_style','user_down_style','weighted_score','age_in_days','number_of_comments',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:allposts", "lookup_field": "title"}
        }
        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        # }
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# class CommentSerializer(serializers.ModelSerializer):
#     children = serializers.SerializerMethodField()
#     owner = serializers.SerializerMethodField()
#     upvotes = serializers.IntegerField(read_only=True)
#     downvotes = serializers.IntegerField(read_only=True)
#     user_vote = serializers.SerializerMethodField()

#     class Meta:
#         model = Comment
#         fields = ["id", "created_date", "owner", "upvotes", "downvotes", "children", "parent_comment", "user_vote"]
#         read_only_fields = ["created", "upvotes", "downvotes"]

#     def get_children(self, obj):
#         children = Comment.objects.filter(parent_comment=obj)
#         return CommentSerializer(children, many=True, context=self.context).data


#     def get_owner(self, obj):
#         return obj.author.username

#     def get_user_vote(self, obj):
#         if not self.context.get('request').user.is_authenticated:
#             return None
#         try:
#             vote = CommentVote.objects.get(user=self.context.get('request').user, comment=obj)
#             return vote.vote_type
#         except CommentVote.DoesNotExist:
#             return None

        # fields = ["id", "created_date", "modified", "content", "owner", "upvotes", "downvotes", "children", "parent_comment", "user_vote"]
        # read_only_fields = ["created", "modified", "upvotes", "downvotes"]

    # def get_children(self, obj):
    #     return CommentSerializer(obj.children.all(), many=True).data

    # def get_owner(self, obj):
    #     if obj.owner:
    #         return obj.owner.username
    #     return ""


class CommentSerializer(serializers.ModelSerializer):
    upvoted_by = serializers.StringRelatedField(many=True, read_only=True)
    downvoted_by = serializers.StringRelatedField(many=True, read_only=True)
    children = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    upvotes = serializers.IntegerField(read_only=True)
    downvotes = serializers.IntegerField(read_only=True)
    user_vote = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "created_date", "owner", "upvotes", "downvotes", "upvoted_by", "downvoted_by", "children", "parent_comment", "user_vote", "text"]
        read_only_fields = ["created", "upvotes", "downvotes", "upvoted_by", "downvoted_by"]

    def get_children(self, obj):
        children = Comment.objects.filter(parent_comment=obj)
        return CommentSerializer(children, many=True, context=self.context).data

    def get_owner(self, obj):
        return obj.author.username

    def get_user_vote(self, obj):
        if not self.context.get('request').user.is_authenticated:
            return None
        try:
            vote = CommentVote.objects.get(user=self.context.get('request').user, comment=obj)
            return vote.vote_type
        except CommentVote.DoesNotExist:
            return None


from rest_framework import serializers
from .models import Reply


class CommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'body', 'created_at']
        read_only_fields = ['id', 'created_at']

# class CommentReplySerializer(serializers.ModelSerializer):
#     parent_reply_id = serializers.PrimaryKeyRelatedField(queryset=Reply.objects.all(), required=False)
#     class Meta:
#         model = Reply
#         fields = ['id', 'user', 'comment', 'body', 'created_at', 'parent_reply_id']
#         read_only_fields = ['id', 'created_at']


