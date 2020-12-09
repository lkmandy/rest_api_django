from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer

# DetailView CreateView FormView
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
        lookup_field  =  'pk'  # slug, id # url(r'?P<pk>\d+')
        serializer_class = BlogPostSerializer
        # queryset  =  BlogPost.objects.all()

        def get_queryset(self):
                return BlogPost.objects.all()


        # def get_object(self):
        #         pk = self.kwargs.get("pk")
        #         return BlogPost.objects.get(pk=pk)

