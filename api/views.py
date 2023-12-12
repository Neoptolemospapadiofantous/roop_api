# your_app_name/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            base_url = "https://api.printify.com/v1"
            shop_id = "13109758"
            api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImRjNGY2YzY0OTAyZTNhNTVmZTYyNzY4ODdhNzc1ODQ1ODA5ZTEzMTg3Y2U4MmNjZDU0ZDM1MWQ4YWFkOTRiZWFlM2NjNjIwZjc5Y2MxM2ZjIiwiaWF0IjoxNzAxODE1NzI2LjI2MDg3NiwibmJmIjoxNzAxODE1NzI2LjI2MDg4LCJleHAiOjE3MzM0MzgxMjYuMjUxNjk4LCJzdWIiOiIxNjE4NDg5NiIsInNjb3BlcyI6WyJzaG9wcy5tYW5hZ2UiLCJzaG9wcy5yZWFkIiwiY2F0YWxvZy5yZWFkIiwib3JkZXJzLnJlYWQiLCJvcmRlcnMud3JpdGUiLCJwcm9kdWN0cy5yZWFkIiwicHJvZHVjdHMud3JpdGUiLCJ3ZWJob29rcy5yZWFkIiwid2ViaG9va3Mud3JpdGUiLCJ1cGxvYWRzLnJlYWQiLCJ1cGxvYWRzLndyaXRlIiwicHJpbnRfcHJvdmlkZXJzLnJlYWQiXX0.AYAfeVwqaMiMUfZN8TSqI07MkB1uK50-xdPXxGBRatnHTH7APU0rAq79hkQOCETh2DR6CuzINmw-wswmsbY"  # Replace with your actual API key
            products_endpoint = f"{base_url}/shops/{shop_id}/products.json"

            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.get(products_endpoint, headers=headers)

            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

            products = response.json().get("data", [])
            return Response({"products": products}, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({"error": f"Failed to fetch products. Details: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)