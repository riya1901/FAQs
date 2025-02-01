from django.urls import path
from .views import FAQList, FAQDetail
app_name = 'faqs' 
urlpatterns = [
    path('faqs/', FAQList.as_view(), name='faq-list'),
    # path('faqs/<int:pk>/', FAQDetail.as_view(), name='faq-detail'),
]
