import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .decorators import validate_api_key
import json
from .plugins.chart import save_chart
from .links.views import get_link_price_and_data_list_for_the_last_month
from .model import PriceChartData
from .helpers import build_validation_error
from pydantic import ValidationError
from asgiref.sync import async_to_sync, sync_to_async

async def handle_post_request(data):
    link_id = data.get('linkId')
    link_data = await get_link_price_and_data_list_for_the_last_month(link_id)

    temp_filepath = save_chart(link_data['dates'], link_data['prices'], link_data['title'])

    return {
        'messages': 'Chart successfully generated',
        'chartUrl': temp_filepath
    }

@sync_to_async
@csrf_exempt
@validate_api_key
@async_to_sync
async def price_chart(request):
    if request.method == 'POST':
        try:
            data = PriceChartData.parse_raw(request.body.decode('utf-8'))
            response_data = await handle_post_request(data.dict())
            return JsonResponse(response_data)
        except ValidationError as validation_error:
            return JsonResponse(build_validation_error(validation_error.errors()), status=400)
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