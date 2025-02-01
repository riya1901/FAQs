


from rest_framework import generics
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQList(generics.ListCreateAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.GET.get('lang', 'en')
        cache_key = f"faq_list_{lang}"

        cached_faqs = cache.get(cache_key)  # Cache check karo
        if cached_faqs:
            return FAQ.objects.filter(id__in=[faq["id"] for faq in cached_faqs])  # JSON से IDs लेके queryset fetch करो

        queryset = FAQ.objects.all()
        serialized_faqs = []

        for faq in queryset:
            faq.question = faq.get_translated_question(lang)  # Translate question
            serialized_faqs.append({"id": faq.id, "question": faq.question, "answer": faq.answer})  # JSON store karne ke liye dict me convert

        cache.set(cache_key, serialized_faqs, timeout=3600)  # Cache for 1 hour
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
            obj.question = cached_faq["question"]
            obj.answer = cached_faq["answer"]
            return obj

        obj.question = obj.get_translated_question(lang)  # Translate question
        cache.set(cache_key, {"question": obj.question, "answer": obj.answer}, timeout=3600)  # JSON store karo
        return obj
