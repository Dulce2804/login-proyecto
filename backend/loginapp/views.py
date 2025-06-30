from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                return JsonResponse({'status': 'ok', 'message': 'Autenticación exitosa'})
            else:
                return JsonResponse({'status': 'fail', 'message': 'Credenciales inválidas'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'message': 'JSON inválido'}, status=400)

    return JsonResponse({'status': 'fail', 'message': 'Método no permitido'}, status=405)
