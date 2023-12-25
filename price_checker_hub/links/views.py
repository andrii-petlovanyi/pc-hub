import asyncio
from .services import get_link_price_list_for_the_last_month

async def get_link_price_and_data_list_for_the_last_month(link_id):
    link_with_price_list = await get_link_price_list_for_the_last_month(link_id)

    dates = [link.createdAt.strftime("%Y-%m-%d") for link in link_with_price_list.priceList]
    prices = [link.price for link in link_with_price_list.priceList]
    title = link_with_price_list.title

    return {'dates': dates, 'prices': prices, 'title':title}
