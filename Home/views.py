from django.shortcuts import render

# Create your views here.
from .models import Contact
import json
from bson import json_util
from rest_framework.response import Response


def create_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        country = request.POST.get('country')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, country=country)
        contact.save()
        response_data = {
            "_id": contact.id,
            "contact": contact.name,
        }
        return Response(
            {
                "status": True,
                "message": f"organization created successfully",
                "response": json.loads(json_util.dumps(response_data)),
            }
        )
