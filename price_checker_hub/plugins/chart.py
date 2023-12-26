from django.conf import settings
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn
from io import BytesIO
from pathlib import Path
from datetime import datetime

def save_chart(dates, prices, title):
    seaborn.set()

    prices = list(map(float, prices))

    plt.plot(dates, prices, linestyle='-', marker='o', color='b', label='Price')
    plt.ylabel('Price')
    plt.xlabel('Date of change price')
    plt.title(title)
    plt.legend()
    plt.xticks(ha='right', rotation=45, fontsize=7)
    plt.yticks(range(int(min(prices)), int(max(prices)+5), 5))
    plt.subplots_adjust(bottom=0.2)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    invalid_chars = [' ', '\\', '|', '/', "'", '"']
    for char in invalid_chars:
        title = title.replace(char, '-')

    temp_filename = f'chart_{title}_{current_date}.png'
    charts_dir = Path(settings.MEDIA_ROOT) / 'charts'

    if not charts_dir.is_dir():
        charts_dir.mkdir(parents=True)

    temp_filepath = charts_dir / temp_filename

    with open(temp_filepath, 'wb') as temp_file:
        temp_file.write(buffer.read())

    return str(temp_filepath.relative_to(settings.MEDIA_ROOT))
