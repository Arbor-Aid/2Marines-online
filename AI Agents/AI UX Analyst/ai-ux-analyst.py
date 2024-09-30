import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Sample UX data for analysis (replace with actual UX data)
data = {
    'session_duration': [5, 10, 7, 15, 20, 12],
    'click_through_rate': [0.1, 0.2, 0.15, 0.4, 0.3, 0.25],
    'page_interaction': [50, 80, 60, 100, 120, 75],
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Standardize the data for better AI processing
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Apply KMeans clustering to group user experiences
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels to the original data
df['cluster'] = clusters

# Calculate the Silhouette Score to evaluate the clustering quality
silhouette_avg = silhouette_score(scaled_data, clusters)
print(f"Silhouette Score: {silhouette_avg}")

# AI-Driven insights
def generate_ux_insights(cluster_data):
    for cluster_id, group in cluster_data.groupby('cluster'):
        print(f"\nCluster {cluster_id}:")
        print(f"Average Session Duration: {group['session_duration'].mean()} mins")
        print(f"Average Click Through Rate: {group['click_through_rate'].mean()}")
        print(f"Average Page Interaction: {group['page_interaction'].mean()}")
        
        # AI-suggested improvements
        if group['click_through_rate'].mean() < 0.2:
            print("Recommendation: Consider improving call-to-action visibility.")
        if group['session_duration'].mean() < 10:
            print("Recommendation: Optimize page load speed or make content more engaging.")

# Run the insights generation function
generate_ux_insights(df)
