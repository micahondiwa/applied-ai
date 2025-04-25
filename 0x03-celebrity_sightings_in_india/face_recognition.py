# Import needed libraries

# Load MTCNN, Resnet, and the embedding data

mtcnn = ...

resnet = ...
embedding_data = ...

resnet = resnet.eval()


# Fill in the locate_face function
def locate_faces(image):
    ...
    


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
