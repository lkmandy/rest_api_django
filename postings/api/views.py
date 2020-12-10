from rest_framework import generics, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer

# Create View
class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
        lookup_field  =  'pk'  # slug, id # url(r'?P<pk>\d+')
        serializer_class = BlogPostSerializer
        # queryset  =  BlogPost.objects.all()

        def get_queryset(self):
                return BlogPost.objects.all()
        
        def perform_create(self, serializer):
                serializer.save(user=self.request.user)
        
        def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)


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

