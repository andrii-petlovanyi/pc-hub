import asyncio
from django.http import JsonResponse
from datetime import datetime, timedelta
from prisma import Prisma

async def get_link_price_list_for_the_last_month(link_id):
    try:
        prisma = Prisma()
        await prisma.connect()

        thirty_days_ago = datetime.now() - timedelta(days=30)

        item_link_with_recent_prices = await prisma.itemlink.find_unique(
            where={
                "id": link_id,
            },
            include={"priceList": {
                "where": {"createdAt": {"gte": thirty_days_ago}},
            }},
        )

        if item_link_with_recent_prices.id:
            return item_link_with_recent_prices
        else:
            raise JsonResponse({'message':f'Not found link with id: {link_id}'})
    except Exception as e:
        raise JsonResponse(f"Error: {e}")

    finally:
        await prisma.disconnect()

