from django.http import JsonResponse
from sklearn.cluster import KMeans
import pandas as pd

def cluster_data(request):
    if request.method == 'POST':
        file = request.FILES['file']
        data = pd.read_csv(file)

        # Assuming number_of_clusters is passed as a parameter
        number_of_clusters = int(request.POST.get('number_of_cluster', 3))
        
        # Drop non-numeric columns
        numeric_data = data.select_dtypes(include=['number'])

        if numeric_data.empty:
            return JsonResponse({'error': 'No numeric data found in the file'}, status=400)

        kmeans = KMeans(n_clusters=number_of_clusters)
        kmeans.fit(numeric_data)
        labels = kmeans.labels_

        # Rename columns to 'x' and 'y'
        numeric_data.columns = ['x', 'y']

        # Prepare response data
        response_data = {
            "labels": labels.tolist(),
            "datapoints": numeric_data.to_dict(orient='records')
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
