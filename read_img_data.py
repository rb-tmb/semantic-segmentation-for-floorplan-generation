import argparse
import numpy as np
from PIL import Image

parser = argparse.ArgumentParser(
        description="PyTorch Semantic Segmentation Testing"
    )
parser.add_argument(
    "--file_inp",
    required=True,
    type=str,
    help="path for input file, or a directory name"
)

args = parser.parse_args()

print("Loading data from file....")
# Read the array from disk
new_data = np.loadtxt(args.file_inp)

# Note that this returned a 2D array!
print("New Data is in Shape: ",new_data.shape)

# However, going back to 3D is easy if we know the 
# original shape of the array
print("Reshaping to original img_array size: (600, 525, 3)")
new_data = new_data.reshape((600, 525, 3))
img_data = (new_data*255).astype('uint8')
img = Image.fromarray(img_data).save("generated_img_data.png")
imag = Image.open("generated_img_data.png")
imag.show()
print("Done!!")

#To run this file use this in command line: python3 read_img_data.py --file_inp img_data/img1_array.txt