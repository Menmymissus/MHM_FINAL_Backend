import pandas as pd
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StressLevelInputSerializer
# Import your ML model
from joblib import load
model = load('stress_model.joblib')

@api_view(['POST'])
def predict_stress_level(request):
    serializer = StressLevelInputSerializer(data=request.data)
    
    if serializer.is_valid():
        # Extract data from the serializer
        input_data = serializer.validated_data
    
        # Convert the input data to a DataFrame (required format for the model)
        input_df = pd.DataFrame([input_data])
        # Preprocess data and pass it to the ML model for prediction
        result = model.predict(input_df)[0]
        print(result)
        return Response({"result": result}, status=status.HTTP_200_OK)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
