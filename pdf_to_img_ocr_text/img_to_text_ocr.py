#!pip install easyocr

from easyocr import Reader
from PIL import Image
from io import BytesIO
# Load model for the English language
language_reader = Reader(["en"])

#Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.

def ocr_image(img_file_path):
   
   image = Image.open(BytesIO(img_file_path))
   raw_text = language_reader.readtext(img_file_path)
   raw_text = "\n".join([res[1] for res in raw_text])
   image_content.append(raw_text)
   print(image_content)
    #return "\n".join(image_content)

text_with_easy_ocr = ocr_image(["Figure_1.png"])
print(text_with_easy_ocr)


