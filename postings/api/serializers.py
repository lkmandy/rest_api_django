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
                read_only_fields = ['user']
        def validate_title(self, value):
                qs = BlogPost.objects.filter(title__iexact=value)
                if self.instance:
                        qs = qs.exclude(pk=self.instance.pk)
                if qs.exists():
                        raise serializers.ValidationError("This title has already been used")

