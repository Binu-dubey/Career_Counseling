from django.urls import path
from .views import GenerateTest, SubmitTest

urlpatterns = [
    path('generate-test/<str:test_type>/', GenerateTest.as_view(), name='generate_test'),
    path('submit-test/', SubmitTest.as_view(), name='submit_test'),
]
