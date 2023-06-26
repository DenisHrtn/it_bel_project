from django.shortcuts import render
from rest_framework.views import APIView


class ContactView(APIView):
    def get(self, request):
        return render(request, "contact.html")
