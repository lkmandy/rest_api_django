from rest_framework import serializers

from postings.models import BlogPost

# forms.ModelForm
class BlogPostSerializer(serializers.ModelSerializer):
        class Meta:
                model = BlogPost
                fields = [
                        'pk',
                        'user',
                        'title',
                        'content',
                        'timestamp',
                ]