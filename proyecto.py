import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
df = pd.read_csv("data.csv")

print("=" * 50)
print("ANÁLISIS DE CANCIONES Y POPULARIDAD")
print("=" * 50)

# Información general
print("\nNúmero de registros:", len(df))
print("Número de columnas:", len(df.columns))

print("\nColumnas del dataset:")
print(df.columns.tolist())

# Mostrar las primeras canciones
print("\nPrimeras 5 canciones:")
print(df[["artist name", "song name"]].head())

# Artistas con más canciones
artistas = df["artist name"].value_counts().head(10)

print("\nTop 10 artistas con más canciones:")
print(artistas)

# Canciones con más streams
top_streams = df.sort_values("total", ascending=False).head(10)

print("\nTop 10 canciones con más streams:")
print(top_streams[["artist name", "song name", "total"]])

# Estadísticas
print("\nEstadísticas de semanas en listas:")
print(df["wks"].describe())

# Gráfica de artistas con más canciones
plt.figure(figsize=(10, 6))
artistas.sort_values().plot(kind="barh")
plt.title("Top 10 artistas con más canciones")
plt.xlabel("Número de canciones")
plt.ylabel("Artista")
plt.tight_layout()
plt.savefig("grafica_artistas.png")
plt.close()

# Gráfica de las canciones con más streams
plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_streams,
    x="total",
    y="song name"
)
plt.title("Top 10 canciones con más streams")
plt.xlabel("Streams")
plt.ylabel("Canción")
plt.tight_layout()
plt.savefig("grafica_streams.png")
plt.close()

# Resumen de resultados
artista_principal = artistas.index[0]
cancion_principal = top_streams.iloc[0]["song name"]
artista_cancion_principal = top_streams.iloc[0]["artist name"]

print("\nRESUMEN DE RESULTADOS")
print("-" * 30)
print(f"Artista con más canciones en el dataset: {artista_principal}")
print(f"Canción con más streams: {cancion_principal}")
print(f"Artista de la canción más reproducida: {artista_cancion_principal}")
print(f"Promedio de semanas en listas: {df['wks'].mean():.2f}")

print("\nAnálisis terminado correctamente.")
