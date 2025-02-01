
# from rest_framework import generics
# from .models import FAQ
# from .serializers import FAQSerializer

# class FAQList(generics.ListCreateAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer

# class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer
from rest_framework import generics
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQList(generics.ListCreateAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.GET.get('lang', 'en')
        cache_key = f"faq_list_{lang}"

        cached_faqs = cache.get(cache_key)  # Check cache
        if cached_faqs:
            return cached_faqs  # Return cached data

        queryset = FAQ.objects.all()
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)  # Get translated question

        cache.set(cache_key, queryset, timeout=3600)  # Cache for 1 hour
        return queryset

class FAQDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

    def get_object(self):
        obj = super().get_object()
        lang = self.request.GET.get('lang', 'en')
        cache_key = f"faq_{obj.id}_{lang}"

        cached_faq = cache.get(cache_key)
        if cached_faq:
            return cached_faq

        obj.question = obj.get_translated_question(lang)  # Translate question
        cache.set(cache_key, obj, timeout=3600)  # Cache object for 1 hour
        return obj
