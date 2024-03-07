import PIL.Image 
img=PIL.Image.open('image.jpg')
model=genai.GenerativeModel('gemini-pro-vision') 
response=model.generate_content(img) to_markdown(response.text)
