from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .plugins.chart import save_chart

# import asyncio
# from prisma import Prisma

def handle_post_request(data):
    dates = data.get('dates', [])
    prices = data.get('prices', [])
    title = data.get('title')

    temp_filepath = save_chart(dates, prices, title)

    return {
        'messages': 'Chart successfully generated',
        'chartUrl': temp_filepath
    }

@csrf_exempt
def price_chart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            response_data = handle_post_request(data)
            return JsonResponse(response_data)
        except json.JSONDecodeError as json_error:
            return JsonResponse({'messages': f'Error decoding JSON: {json_error}'}, status=400)
        except Exception as e:
            return JsonResponse({'messages': f'Error: {str(e)}', 'chartUrl': None}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

# TODO: temporary example for use Prisma
# @csrf_exempt
# async def users(request):
#     if request.method == 'GET':
#         try:
#             prisma = Prisma()
#             await prisma.connect()

#             users = await prisma.user.find_many()
#             users_dict = [{'id': user.id, 'telegramId': user.telegramId, 'nickname': user.nickname} for user in users]

#             return JsonResponse(users_dict, safe=False)

#             await prisma.disconnect()
#         except json.JSONDecodeError as json_error:
#             return JsonResponse({'messages': f'Error decoding JSON: {json_error}'}, status=400)
#         except Exception as e:
#             return JsonResponse({'messages': f'Error: {str(e)}'}, status=400)
#     else:
#         return JsonResponse({'status':'error', 'message': 'Invalid request message'}, status=400)