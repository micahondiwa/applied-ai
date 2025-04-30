# Import needed libraries
import streamlit as st

# Task 5.4.2: Fill in the app.py file with imports and model_ids list.
import torchvision
from medigan import Generators
from torchvision.transforms.functional import to_pil_image
from torchvision.utils import make_grid
# Define the GAN models available in the app
model_ids = [
    "00001_DCGAN_MMG_CALC_ROI",
    "00002_DCGAN_MMG_MASS_ROI",
    "00003_CYCLEGAN_MMG_DENSITY_FULL",
    "00004_PIX2PIX_MMG_MASSES_W_MASKS",
    "00019_PGGAN_CHEST_XRAY",
]

def main():
    st.title("MEDIGAN Medical Image Data Generator")

    # Add dropdown widget for model selection to the sidebar
    model_id = st.sidebar.selectbox("Select Model ID", model_ids)

    # Add number image selector to the sidebar
    # Task 5.4.3: Add values for the keyword arguments min_value= and max_value= in the st.sidebar.number_input function call in the main function.
    num_images = st.sidebar.number_input(
        "Number of Images", min_value=..., max_value=..., value=1, step=1
    )


    # Add generate button to the sidebar
    if st.sidebar.button("Generate Images"):
        # Task 5.4.12: Add the parameters to the generate_images function call in the st.sidebar.button function call in the main function.
        generate_images(...)


# Task 5.4.9: Copy the torch_images function from this notebook to app.py.
def torch_images(num_images, model_id):
    ...


def generate_images(num_images, model_id):
    st.subheader("Generated Images:")
    # Task 5.4.11: Add the parameters to the torch_images function call in the generate_images function.
    images = torch_images(...)
    for i in range(len(images)):
        # Display generated images in the web app
        st.image(
            images[i],
            caption=f"Generated Image {i+1} (Model ID: {model_id})",
            use_container_width=True,
        )


if __name__ == "__main__":
    # Task 5.4.4: Add a call to the main function in the main block.
    ...
