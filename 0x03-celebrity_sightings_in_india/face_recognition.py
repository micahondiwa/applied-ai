# Import needed libraries
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt 
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image

# Load MTCNN, Resnet, and the embedding data
mtcnn = MTCNN(image_size=240, keep_all=True, min_face_size=40)

resnet = InceptionResnetV1(pretrained="vggface2")

embedding_data = torch.load("embeddings.pt")

resnet = resnet.eval()


# Fill in the locate_face function

def locate_faces(image):
    cropped_images, probs = mtcnn(image, return_prob=True)
    boxes, _ = mtcnn.detect(image)

    if boxes is None or cropped_images is None:
        return []
    else:
        return list(zip(boxes, probs, cropped_images))


# Fill in the determine_name_dist function
def determine_name_dist(cropped_image, threshold=0.9):
    ...
    


# Fill in the label_face function
def label_face(name, dist, box, axis):
    ...
    


# Fill in the add_labels_to_image function
def add_labels_to_image(image):
    ...


# This file © 2024 by WorldQuant University is licensed under CC BY-NC-ND 4.0.
