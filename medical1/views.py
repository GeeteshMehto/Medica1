from django.shortcuts import render, redirect
import numpy as np
import json
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
from keras.models import load_model
from django.contrib import messages
from tensorflow.keras.utils import img_to_array, load_img
import random


def index(request):
    # value = random.choice(['yes', 'no'])
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')



# acc = model.evaluate_generator()
#
# ref = dict(zip(list(train.class_indices.values()), list(train.class_indices.keys())))

# with open("ref_kv.json", "w") as fp:
#     json.dump(ref, fp)



def prediction(path):
    model = load_model("Medical/static/best_model_f.h5")

    with open('Medical/static/ref_breast.json') as json_file:
        ref = json.load(json_file)

    img = load_img(path, target_size=(256, 256))

    i = img_to_array(img)

    im = preprocess_input(i)

    img = np.expand_dims(im, axis=0)

    pred = np.argmax(model.predict(img))

    return(f"The image belongs to {ref[str(pred)]}")

def breastc(request):
    if request.method == "POST":
        imgy = request.POST["breastc"]
        print("---------------------")
        print(imgy)
        print("---------------------")

    # model = load_model("best_model_f.h5")
    # # # acc = model.evaluate_generator()
    # #
    # # ref = dict(zip(list(train.class_indices.values()), list(train.class_indices.keys())))
    #
    # # with open("ref_kv.json", "w") as fp:
    # #     json.dump(ref, fp)
    #
    # with open('ref_breast.json') as json_file:
    #     ref = json.load(json_file)
    #
    # def prediction(path):
    #     img = load_img(path, target_size=(256, 256))
    #
    #     i = img_to_array(img)
    #
    #     im = preprocess_input(i)
    #
    #     img = np.expand_dims(im, axis=0)
    #
    #     pred = np.argmax(model.predict(img))
    #
    #     return(f"The image belongs to {ref[str(pred)]}")
    #     # print(f"The image belongs to {ref[pred]}")

    path = "Medical/static/images/WhatsApp Image 2023-04-02 at 3.26.22 AM.jpeg"
    kk = prediction(path)
    # prediction(path)
    messages.success(request, f"Your result is {kk}")
    print(kk)

    return redirect("/")
