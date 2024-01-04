from django.conf import settings
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn
from io import BytesIO
from pathlib import Path
from datetime import datetime
import numpy as np

def save_chart(dates, prices, title):
    background_color = '#202946'
    grid_color = '#2a3459'
    bg_color = '#08F7FE'
    plot_color = '#08F7FE99'
    legend_color = '#404966'
    text_color = '#ffffff'

    seaborn.set(style="whitegrid", rc={"grid.color": grid_color})
    fig, ax = plt.subplots(figsize=(8, 6), facecolor=background_color)
    fig.patch.set_facecolor(background_color)

    prices = list(map(float, prices))

    plt.plot(dates, prices, linestyle='-', marker='o', color=plot_color, label='Price')
    plt.ylabel('Price', color=text_color)
    plt.xlabel('Date', color=text_color)
    plt.title(title, color=text_color)
    plt.legend(facecolor=legend_color, edgecolor=legend_color, labelcolor=text_color, loc='upper right')
    plt.xticks(ha='right', rotation=45, fontsize=7, color=text_color)
    plt.yticks(range(int(min(prices)), int(max(prices)+5), 5), color=text_color)
    plt.subplots_adjust(bottom=0.2)

    ax.set_facecolor(background_color)
    ax.set_frame_on(False)
    fill_bottom = min(prices) - 5
    fill_top = max(prices) + 5
    mask = np.array(prices) >= fill_bottom
    ax.fill_between(dates, fill_bottom, prices, color=bg_color, alpha=0.04, where=mask, interpolate=True)
    ax.set_ylim(fill_bottom, fill_top)

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
