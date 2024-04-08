# This program will take a pdf with an images embedded and then extract the images and then use OCR to extract the text from the images
if you are looking at Llama2 Rag implimentation look at my implimentation here https://github.com/antonjan/local_ai_with_pdf

## Usage
you need to add two parameters the inputfile witch should be pdf with images embedid with in them and output file where the Text will be saved

    python3 ./img_pdf_langchange_to_text.py img_pdf.pdf output.txt
  
### Image exsample
![Screenshot of the image in the pdf.](https://github.com/antonjan/AI-with-opencv/blob/main/pdf_to_img_ocr_text/Figure_1.png)

### Text extract
  
    ~~ Page Number 1 -—~

    This document provides a quick summary of some of Zoumana'’s article on Medium. It can be considered as the compilation of his 80+ articles about Data Science, Machine Learning and

            Machine Learning Operations.
            
            Whether you are just getting started or you're an experienced professional looking to upskill, these
            
            materials can be helpful.
            
            Data Science section covers basic to advanced concepts such as statistics, model evaluation metrics, SQL queries, NOSQL courses, data visualization using Tableau and #powerbi, and many more.
            
            Link: httos://Inkd.in/g8zcS_vE
            
            MLOps chapter explains how to build and deploy models using different strategies such as Docker containers, and GitHub actions on AWS EC2 instances, Azure. Also, it covers how to build REST APIs to serve your models.
            
            Link: httos://Inkd.in/qyiUsdgz
            
            Natural Language Processing Covers simple NLP concepts to more advanced ones such as Transformers and their applications in Finance, Science, etc.
            
            Link: httos://Inkd.in/gBdZbHty
            
            Computer Vision section covers SOTA models (e.g. YOLO) and different technics to mitigate
            
            overfitting when training computer vision models.
            
            Link: https://Inkd.in/gDY8ZqVs
            
            Python section showcases multiple libraries to facilitate one's daily life, especially when dealing with PDF, and Word files when scraping data from the web, and even benchmarking analysis to help choose the right data processing tool.
            
            Link: https://Inkd.in/QH HUMM9
            
            Pandas & Python Tricks Covers my daily tips and tricks on Linkedin. And, there are plenty of those, especially on my
            
            website https://Inkd.in/gPbichBS https://Inkd.in/gUs8inuZ
            
            Machine Learning part is about Fexplainable Al, clustering, classification tasks, etc.
            
            Link: https://Inkd.in/gJdSvQns~~ Page Number 1 -—~
            
            This document provides a quick summary of some of Zoumana'’s article on Medium. It can be considered as the compilation of his 80+ articles about Data Science, Machine Learning and
            
            Machine Learning Operations.
            
            Whether you are just getting started or you're an experienced professional looking to upskill, these
            
            materials can be helpful.
            
            Data Science section covers basic to advanced concepts such as statistics, model evaluation metrics, SQL queries, NOSQL courses, data visualization using Tableau and #powerbi, and many more.
            
            Link: httos://Inkd.in/g8zcS_vE
            
            MLOps chapter explains how to build and deploy models using different strategies such as Docker containers, and GitHub actions on AWS EC2 instances, Azure. Also, it covers how to build REST APIs to serve your models.
            
            Link: httos://Inkd.in/qyiUsdgz
            
            Natural Language Processing Covers simple NLP concepts to more advanced ones such as Transformers and their applications in Finance, Science, etc.
            
            Link: httos://Inkd.in/gBdZbHty
            
            Computer Vision section covers SOTA models (e.g. YOLO) and different technics to mitigate
            
            overfitting when training computer vision models.
            
            Link: https://Inkd.in/gDY8ZqVs
            
            Python section showcases multiple libraries to facilitate one's daily life, especially when dealing with PDF, and Word files when scraping data from the web, and even benchmarking analysis to help choose the right data processing tool.
            
            Link: https://Inkd.in/QH HUMM9
            
            Pandas & Python Tricks Covers my daily tips and tricks on Linkedin. And, there are plenty of those, especially on my
            
            website https://Inkd.in/gPbichBS https://Inkd.in/gUs8inuZ
            
            Machine Learning part is about Fexplainable Al, clustering, classification tasks, etc.
            
            Link: https://Inkd.in/gJdSvQns

## Deplyment
You need python3 I was using 3.11
install the below dependicy file
using the command pip3 install [file]

## dependincy for project
    easyocr==1.7.1
    langchain==0.1.14
    langchain_community==0.0.31
    matplotlib==3.8.2
    Pillow==10.3.0
    pip==23.3.2
    pypdfium2==4.28.0
    pytesseract==0.3.10
    
    
## dependency
        pip3 install pypdfium2
        pip3 install pytesseract
        pip3 install easyocr
        pip3 install langchain
        pip3 install langchain-community
        pip3 install unstructured
        pip3 install "unstructured[pdf]"
        pip3 install pytesseract
        pip3 install pip install tesseract
        pip3 install tesseract
        pip3 install tesseract-ocr
        sudo apt install libxcb-image0
        sudo apt install libxcb-keysyms1
        sudo apt install libxcb-render-util0
        sudo apt install libxcb-xkb1
        sudo apt install libxkbcommon-x11-0
        sudo apt install python3.8-pip
        sudo apt install libtesseract-dev
        sudo apt-get install tesseract-ocr


