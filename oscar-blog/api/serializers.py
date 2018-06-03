from rest_framework import serializers

from django.contrib.auth.models import User

from appblog.models import Post, Category, CategoryGroup


class PostSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='api:posts-detail',
        lookup_field='pk',
        source='id'
    )

    category = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Category.objects.all(),
        view_name='api:category-blogs',
        lookup_field='pk',
    )

    class Meta:
        model = Post
        fields = ('id', 'url', 'title', 'content', 'featured_image', 'post_date', 'author', 'category', 'excerpt')

    def create(self, validated_data):
        category_list = validated_data.pop('category')
        print(repr(validated_data))
        post = Post.objects.create(**validated_data)
        for category_item in category_list:
            CategoryGroup.objects.create(post=post, category=category_item)

        return post

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.featured_image = validated_data.get('featured_image', instance.featured_image)
        instance.post_date = validated_data.get('post_date', instance.post_date)
        instance.author = validated_data.get('author', instance.author)
        instance.excerpt = validated_data.get('excerpt', instance.excerpt)
        instance.save()

        existing_category_group_set = CategoryGroup.objects.filter(post__id=instance.id)
        for existing_category_group in existing_category_group_set:
            existing_category_group.delete()

        category_list = validated_data.pop('category')
        for category_item in category_list:
            CategoryGroup.objects.create(post=instance, category=category_item)

        return instance


class CategorySerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='api:categories-detail',
        lookup_field='pk',
        source='id'
    )

    class Meta:
        model = Category
        fields = ('id', 'url', 'name')


class UserLoginSerializer(serializers.ModelSerializer):

    token = serializers.CharField(read_only=True, allow_blank=True)
    username = serializers.CharField(allow_blank=True)
    email = serializers.EmailField(label='Email Address', allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')
