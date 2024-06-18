import os
import shutil
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image as im
from mpl_toolkits.axes_grid1 import ImageGrid

import BingImageCreator as BIC

auth_cookie_SRCHHPGUSR = auth_cookie = "1yFpfZKnRshxnZoae5yjkWG52dr22hP5dv5CXm9VIdaEoPvWI4nrqKe6dNfNeYJ0DWiSxXGoSg_fBeVbzAHOTOI07mvex-LVgM1b0GnNGAVnSjPy-l2BWSzK5ZTbG7A1QV8Jm6A0CZMOCDLTw43tpRu7FxFxJp4yKvOQ4nFSbT_f72jCa-_vVzEHSYP3riAAI52XA1CxK8o8oQaWMnA5tjw"

gen = BIC.ImageGen(auth_cookie, auth_cookie_SRCHHPGUSR)
prompt = "JUUL Vape device portrait"
BLinks = gen.get_images(prompt)

# Save first 3 images to current directory
for idx, link in enumerate(BLinks):
    if idx < 3:  # save only the first 3 images
        image = io.imread(link)
        filename = f"image_{idx + 1}.jpg"
        io.imsave(filename, image)
        plt.imshow(image)
        plt.show()
