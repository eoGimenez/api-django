from django.http import JsonResponse

def api_home(request, *argx, **kwargs):
    return JsonResponse({'message': 'Buenas, probando respuesta JSON'})