

# from django.db import models
# from ckeditor.fields import RichTextField
# from deep_translator import GoogleTranslator

# class FAQ(models.Model):
#     question = models.TextField()
#     answer = RichTextField()  # WYSIWYG Editor for formatted text
#     question_hi = models.TextField(blank=True, null=True)  # Hindi translation
#     question_bn = models.TextField(blank=True, null=True)  # Bengali translation
#     question_es = models.TextField(blank=True, null=True)  # Spanish translation
#     created_at = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         translator = GoogleTranslator(source="auto", target="hi")
#         if not self.question_hi:
#             self.question_hi = translator.translate(self.question)
#         translator.target = "bn"
#         if not self.question_bn:
#             self.question_bn = translator.translate(self.question)
#         translator.target = "es"
#         if not self.question_es:
#             self.question_es = translator.translate(self.question)

#         super().save(*args, **kwargs)

#     def get_translated_question(self, lang):
#         return getattr(self, f'question_{lang}', self.question)

#     def __str__(self):
#         return self.question

from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from deep_translator import GoogleTranslator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    question_es = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        cache.delete("faqs")  # Invalidate cache when FAQ is updated

        if not self.question_hi:
            self.question_hi = GoogleTranslator(source="auto", target="hi").translate(self.question)
        if not self.question_bn:
            self.question_bn = GoogleTranslator(source="auto", target="bn").translate(self.question)
        if not self.question_es:
            self.question_es = GoogleTranslator(source="auto", target="es").translate(self.question)

        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        cached_question = cache.get(f"faq_{self.id}_{lang}")  # Check Redis cache
        if cached_question:
            return cached_question  # Return cached translation

        translated_question = getattr(self, f'question_{lang}', self.question)
        cache.set(f"faq_{self.id}_{lang}", translated_question, timeout=3600)  # Cache for 1 hour
        return translated_question

    def __str__(self):
        return self.question
