import streamlit as st
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Fungsi untuk mengatasi input kosong
def handle_empty_input(input_value):
  try:
    return int(input_value) if input_value else 0
  except ValueError:
    st.error("Silahkan masukkan data yang valid.")
    return 0
  
def elbow_method(dataset):
   # Set Parameter KMEANS
    kmeans_set = {"init":"random", "n_init":10, "max_iter":300, "random_state":42}

    inertias = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, **kmeans_set)
        kmeans.fit(dataset)
        inertias.append(kmeans.inertia_)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot your data on the axis
    ax.plot(range(1, 11), inertias, marker='o')
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('Inertia')
    ax.set_title('Elbow Method for KMeans Clustering')

    # Display the plot in Streamlit
    st.pyplot(fig)

# Kmean
def k_means(n_cluster, dataset):
    kmeans = KMeans(n_clusters = n_cluster, n_init=10, random_state=42)
    kmeans.fit(dataset)
    df_kmeans = dataset
    df_kmeans['cluster_id'] = kmeans.fit_predict(dataset)
    return df_kmeans

# Plotting
def plot(kolom1, kolom2, df):
    # Buat ScatterPlot
    fig, ax = plt.subplots()
    sns.scatterplot(x=kolom1, y=kolom2, hue='cluster_id', data = df, palette='viridis')

    # Judul Label
    ax.set_title(f'Scatter Plot {kolom1} dan {kolom2} berdasarkan Cluster')
    ax.set_xlabel(kolom1)
    ax.set_ylabel(kolom2)

    # Tampilkan Dataset Ori
    st.write("**Hasil Clustering :**")
    st.dataframe(df)

    # Tampilkan plot
    st.pyplot(fig)

def plot3d(kolom1, kolom2, kolom3, df):
    fig = px.scatter_3d(df, x=kolom1, y=kolom2, z=kolom3, color='cluster_id')

    # Tampilkan Dataset Ori
    st.write("**Hasil Clustering :**")
    st.dataframe(df)

    # Display the plot in Streamlit
    st.plotly_chart(fig)

# Auto Input Kmeans
def autoKmeans(kolom1, kolom2, n_cluster, dataset):
    df = k_means(n_cluster, dataset)
    plot(kolom1, kolom2, df)

# Auto Input Kmeans
def autoKmeans3D(kolom1, kolom2, kolom3, n_cluster, dataset):
    df = k_means(n_cluster, dataset)
    plot3d(kolom1, kolom2, kolom3, df)


