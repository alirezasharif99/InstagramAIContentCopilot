from flask import Flask, render_template, request
import os
from skimage import io

# Import your BingImageCreator script (ensure it's in the same directory or properly pathed)
import BingImageCreator as BIC

app = Flask(__name__)

auth_cookie_SRCHHPGUSR = auth_cookie = "1yFpfZKnRshxnZoae5yjkWG52dr22hP5dv5CXm9VIdaEoPvWI4nrqKe6dNfNeYJ0DWiSxXGoSg_fBeVbzAHOTOI07mvex-LVgM1b0GnNGAVnSjPy-l2BWSzK5ZTbG7A1QV8Jm6A0CZMOCDLTw43tpRu7FxFxJp4yKvOQ4nFSbT_f72jCa-_vVzEHSYP3riAAI52XA1CxK8o8oQaWMnA5tjw"
gen = BIC.ImageGen(auth_cookie, auth_cookie_SRCHHPGUSR)  # Initialize this once, outside of route functions

def generate_images_from_prompt(prompt):
    try:
        BLinks = gen.get_images(prompt)
    except Exception as e:
        print("Error in BingImageCreator:", e)
        return []
    
    saved_images = []

    # Save the first 3 images to the server's directory
    for idx, link in enumerate(BLinks):
        if idx < 3:
            image = io.imread(link)
            filename = f"static/image_{idx + 1}.jpg"
            io.imsave(filename, image)
            saved_images.append(filename)

    return saved_images

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        image_paths = generate_images_from_prompt(prompt)
        
        return render_template('index.html', images=image_paths)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
