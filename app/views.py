from django.shortcuts import render #, redirect
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm
import cv2
import os
import urllib.request
import tempfile
import pytesseract
import pyttsx3

import io
import numpy as np
import re

#def index(request):
#   return HttpResponse("<h1>Hello world</h1>")

# merging dynamic and static content called rendering

def index(request):
    text = ""
    if request.method == "POST":
        #text = request.POST['text']
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # extract the uploaded image file object from the form
            #image_file = form.cleaned_data['image']
            image_file = Image.objects.create(photo = form.cleaned_data['photo']) # pehle form.cleaned_data se pehle image= likha tha
            # read the image using OpenCV
            #image_cv2 = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            #print(image_file.photo.path)
            image = cv2.imread(image_file.photo.path)

            config = ('-l eng --oem 1 --psm 3')
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            #global text 
            text = pytesseract.image_to_string(image, config = config)
            text = re.sub('\s+', ' ', text).strip()
            #form.save()
            
    else:
        form = ImageForm()
    
    
    '''
    for pic in img:
        image_url = pic.photo.url
        with urllib.request.urlopen(image_url) as url:
            with tempfile.NamedTemporaryFile(delete=False) as tf:
                tf.write(url.read())
                image_path = tf.name
        # Open the image from the temporary file using PIL
        #pil_image = Image.open(image_path)

        # Convert the PIL image to a numpy array
        #np_image = np.array(pil_image)

        # Convert the numpy array to a cv2 image
        #cv2_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)

        #picture = cv2.imread(image_path)
        #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        #text = pytesseract.image_to_string(cv2_image, config = config)
    '''
    obj = pyttsx3.init()
    obj.setProperty('rate', 150)
    obj.say(text)
    obj.runAndWait()
    #os.remove(image_path)
    #'pics':img, 'name':name, 
    img = Image.objects.all()
    return render(request , 'index.html', {'form':form, 'img_text':text, 'pics':img})


def result(request):
    text = request.POST['text']
    obj = pyttsx3.init()
    obj.setProperty('rate', 150)
    obj.say(text)
    obj.runAndWait()
    return render(request, 'result.html', {'text' : text})