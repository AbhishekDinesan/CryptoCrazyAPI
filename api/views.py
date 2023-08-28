#create all of YOUR ENDPOINTS
from django.http import JsonResponse
from .models import crypto
from .serializers import CryptoSerializer

def crypto_list(request):
    c = crypto.objects.all()
    s = CryptoSerializer(c, many = True)
    return JsonResponse({"crypto": s.data}, safe = False)
    