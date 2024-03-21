#!pip install langchain
#import UnstructuredFileLoader
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.document_loaders.image import UnstructuredImageLoader
import sys

def extract_text_with_langchain_image(list_dict_final_images):
    
    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []
    
    for index, image_bytes in enumerate(image_list):
        
        image = Image.open(BytesIO(image_bytes))
        loader = UnstructuredImageLoader(image)
        data = loader.load()
        raw_text = data[index].page_content
                       
        image_content.append(raw_text)
    
    return "\n".join(image_content)

#text_with_langchain_image = extract_text_with_langchain_image(convert_pdf_to_images)
#print(text_with_langchain_image)

from langchain.document_loaders import UnstructuredFileLoader

def extract_text_with_langchain_pdf(pdf_file):
    
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)
    
    return pdf_pages_content


args = len(sys.argv) - 1
pos = 1
while (args >= pos):
    print ("Parameter at position %i is %s" % (pos, sys.argv[pos]))
    pos = pos + 1
    #text_with_langchain_files = extract_text_with_langchain_pdf("img_pdf.pdf")
    text_with_langchain_files = extract_text_with_langchain_pdf(sys.argv[1])
    f= open(sys.argv[2],"a+")
    f.write(text_with_langchain_files)
f.close()    
print ("The script was called with %i arguments" % (args))

print(text_with_langchain_files)


