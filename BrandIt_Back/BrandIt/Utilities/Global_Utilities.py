from django.core import exceptions

image_extensions = ['jpg', 'png', 'jpeg', 'JPG', 'JPEG', 'PNG']
allowed_image_extensions_msg = "Allowed Formats : '.jpg/.jpeg', '.png'"

def FileSize(value):
    limit = 5 * (1024**2) # 5 MB
    if value.size > limit:
        return exceptions.ValidationError("Too Large! This file should not exceed 5MB.")

