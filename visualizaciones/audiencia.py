import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import numpy as np
import os

# 1. Carga de datos
df_shows = pd.read_csv('../datasets/tv_show_links.csv')
df_critics = pd.read_csv('../datasets/critic_reviews.csv')
df_audience = pd.read_csv('../datasets/audience_reviews.csv')

# 2. Limpieza de puntajes, para dejar solo valores validos
df_shows['Critic Score'] = pd.to_numeric(df_shows['Critic Score'].str.replace('%',''), errors='coerce')
df_shows['Audience Score'] = pd.to_numeric(df_shows['Audience Score'].str.replace('%',''), errors='coerce')

# Eliminar las filas que quedaron con valores nulos para que no den error al graficar
df_shows = df_shows.dropna(subset=['Critic Score', 'Audience Score'])

# 3. Procesamiento de Sentimiento (Criterio 2)
def get_avg_sentiment(show_name):
    revs = pd.concat([df_critics[df_critics['Show']==show_name]['Review'], 
                      df_audience[df_audience['Show']==show_name]['Review']])
    polarities = [TextBlob(str(r)).sentiment.polarity for r in revs if pd.notna(r)]
    return np.mean(polarities) if polarities else 0

# Seleccionamos una muestra representativa de los datos para graficar
sample_shows = ["13 Reasons Why", "30 Rock", "24", "11.22.63", "A Teacher", "Severance", "Succession", "The Bear", "Dark"]
df_plot = df_shows[df_shows['Show'].isin(sample_shows)].drop_duplicates('Show').copy()
df_plot['Sentiment'] = df_plot['Show'].apply(get_avg_sentiment)
df_plot = df_plot.sort_values('Audience Score')

# 4. Visualización: Dumbbell Plot
fig, ax = plt.subplots(figsize=(10, 7))
cmap = plt.cm.RdYlGn # Rojo (Negativo) a Verde (Positivo)
norm = plt.Normalize(df_plot['Sentiment'].min(), df_plot['Sentiment'].max())

for i, (idx, row) in enumerate(df_plot.iterrows()):
    color = cmap(norm(row['Sentiment']))
    # Línea (La Brecha - Criterio 1)
    ax.plot([row['Critic Score'], row['Audience Score']], [i, i], color=color, linewidth=4, alpha=0.6)
    # Puntos
    ax.scatter(row['Critic Score'], i, color='grey', s=100, label='Crítica' if i==0 else "", zorder=3)
    ax.scatter(row['Audience Score'], i, color='black', s=100, label='Audiencia' if i==0 else "", zorder=3)
    # Texto de Sentimiento (Criterio 2)
    ax.text(102, i, f"Sent: {row['Sentiment']:.2f}", va='center', color=color, fontweight='bold')

ax.set_yticks(range(len(df_plot)))
ax.set_yticklabels(df_plot['Show'])
ax.set_title('Análisis de Disonancia: Brecha de Puntaje y Sentimiento de Reseñas', pad=20)
ax.set_xlabel('Puntaje (0-100)')
ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig('visualizacion_final_fco.png')