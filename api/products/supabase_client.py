# products/supabase_client.py
import os
from supabase import create_client
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
print(supabase, flush=True)

def check_connection():
    try:
        response = supabase.table('products').select("count", count='exact').execute()
        print("Connection successful. Total records:", response.count)
    except Exception as e:
        print("Connection failed:", str(e))


import logging

logger = logging.getLogger(__name__)

import time

def upload_image_to_storage(file, path: str = "product-images/"):
    bucket = "product-images"
    unique_name = f"{path}{int(time.time())}_{file.name}"
    logger.debug("Uploading file with unique name: %s", unique_name)
    file_bytes = file.read()
    if not file_bytes:
        raise Exception("Empty file or unable to read file content")
    file.seek(0)
    result = supabase.storage.from_(bucket).upload(unique_name, file_bytes, {"content-type": file.content_type})
    logger.debug("Upload result: %s", result)
    if hasattr(result, "error") and result.error:
        raise Exception(f"Storage upload error: {result.error.message}")
    public_url = supabase.storage.from_(bucket).get_public_url(unique_name)
    logger.debug("Public URL: %s", public_url)
    return public_url



def create_product_in_supabase(product_data: dict):
    logging.debug("Oh hai!")
    response = supabase.table("products").insert(product_data).execute()
    if response.data:
        return response.data
    else:
        raise Exception("Supabase Error (create): " + str(response.error))

def fetch_products_from_supabase():
    response = supabase.table("products").select("*").execute()
    if response.data:
        return response.data
    else:
        raise Exception("Supabase Error (fetch): " + str(response.error))

def update_product_in_supabase(product_id: int, product_data: dict):
    response = supabase.table("products").update(product_data).eq("id", product_id).execute()
    if response.data:
        return response.data
    else:
        raise Exception("Supabase Error (update): " + str(response.error))

def delete_product_in_supabase(product_id: int):
    # First, fetch the product to get the associated image URL.
    fetch_response = supabase.table("products") \
                               .select("image_url") \
                               .eq("id", product_id) \
                               .single() \
                               .execute()

    if fetch_response.data:
        image_url = fetch_response.data.get("image_url")
        if image_url:

            filename = image_url.split("/")[-1]
            bucket = "product-images"
            # Remove expects a list of file paths.
            delete_result = supabase.storage.from_(bucket).remove([filename])
            logger.debug("Image deletion result: %s", delete_result)
            if hasattr(delete_result, "error") and delete_result.error:
                raise Exception("Error deleting image from bucket: " + str(delete_result.error))
    else:
        logger.debug("No product data found when fetching image URL for product id %s", product_id)
    
    # Now delete the product record
    delete_response = supabase.table("products").delete().eq("id", product_id).execute()
    
    if delete_response.data:
        return delete_response.data
    else:
        raise Exception("Supabase Error (delete): " + str(delete_response.error))
