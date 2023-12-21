import os
from django.conf import settings
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import JsonResponse
import seaborn
from io import BytesIO
from pathlib import Path

def save_chart(dates, prices, title):
    seaborn.set()
    plt.plot(dates, prices, linestyle='-', marker='o', color='b', label='Price')
    plt.ylabel('Price')
    plt.xlabel('Date of change price')
    plt.title(title)
    plt.legend()
    plt.xticks(ha='right', rotation=45, fontsize=7)
    plt.subplots_adjust(bottom=0.2)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    temp_filename = f'chart_{title}.png'
    charts_dir = Path(settings.MEDIA_ROOT) / 'charts'

    if not charts_dir.is_dir():
        charts_dir.mkdir(parents=True)

    temp_filepath = charts_dir / temp_filename

    with open(temp_filepath, 'wb') as temp_file:
        temp_file.write(buffer.read())

    return str(temp_filepath.relative_to(settings.MEDIA_ROOT))
