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
plt.show()

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
plt.show()

print("\nAnálisis terminado correctamente.")
