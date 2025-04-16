# # products/views_supabase.py
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .serializers import ProductSerializer
# from rest_framework.parsers import MultiPartParser, FormParser
# from django.views.decorators.csrf import csrf_exempt
# from .supabase_client import (
#     create_product_in_supabase, 
#     fetch_products_from_supabase, 
#     update_product_in_supabase, 
#     delete_product_in_supabase,
#     upload_image_to_storage
# )
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# class ProductSupabaseViewSet(viewsets.ViewSet):
#     parser_classes = [MultiPartParser, FormParser]  # For handling file upload
#     def list(self, request):
#         try:
#             products = fetch_products_from_supabase()
#             return Response(products, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def create(self, request):
#         logger.debug("Request FILES: %s", request.FILES)
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             product_data = serializer.validated_data
#             if 'image' in request.FILES:
#                 logger.debug("Image found in FILES: %s", request.FILES['image'].name)
#                 try:
#                     image_file = request.FILES['image']
#                     image_url = upload_image_to_storage(image_file)
#                     logger.debug("Image URL: %s", image_url)
#                     product_data['image_url'] = image_url
#                 except Exception as e:
#                     return Response({"error": f"Image upload failed: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             else:
#                 logger.debug("No image found in request.FILES.")
            
#             try:
#                 result = create_product_in_supabase(product_data)
#                 logger.debug("Create product result: %s", result)
#                 return Response(result, status=status.HTTP_201_CREATED)
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def update(self, request, pk=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             product_data = serializer.validated_data

#             # Check if a new image is provided
#             if 'image' in request.FILES:
#                 try:
#                     image_file = request.FILES['image']
#                     image_url = upload_image_to_storage(image_file)
#                     product_data['image_url'] = image_url
#                 except Exception as e:
#                     return Response({"error": f"Image upload failed: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#             try:
#                 result = update_product_in_supabase(pk, product_data)
#                 return Response(result, status=status.HTTP_200_OK)
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         try:
#             result = delete_product_in_supabase(pk)
#             return Response(result, status=status.HTTP_204_NO_CONTENT)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
