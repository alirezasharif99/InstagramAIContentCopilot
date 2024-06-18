from flask import Flask, render_template, request, send_from_directory
import os
from skimage import io
import BingImageCreator as BIC
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# GPT-2 function and BingImageCreator integration here
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
auth_cookie_SRCHHPGUSR = auth_cookie = "1yFpfZKnRshxnZoae5yjkWG52dr22hP5dv5CXm9VIdaEoPvWI4nrqKe6dNfNeYJ0DWiSxXGoSg_fBeVbzAHOTOI07mvex-LVgM1b0GnNGAVnSjPy-l2BWSzK5ZTbG7A1QV8Jm6A0CZMOCDLTw43tpRu7FxFxJp4yKvOQ4nFSbT_f72jCa-_vVzEHSYP3riAAI52XA1CxK8o8oQaWMnA5tjw"



app = Flask(__name__)

def generate_caption(topic, tone, genre, length):
    # Constructing the prompt using user inputs
    prompt = f"Write a {tone} {genre} caption about {topic} that is approximately {length} words long."
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    max_tokens = length * 5  

    output = model.generate(
        input_ids,
        max_length=max_tokens,
        num_return_sequences=5,
        temperature=0.7,
        do_sample=True,
        top_k=50
    )

    captions = [tokenizer.decode(o, skip_special_tokens=True) for o in output]
    return captions


def generate_images_from_prompt(prompt):
    gen = BIC.ImageGen(auth_cookie, auth_cookie_SRCHHPGUSR)
    BLinks = gen.get_images(prompt)
    saved_images_paths = []

    # Save first 3 images to the static/images directory
    for idx, link in enumerate(BLinks):
        if idx < 3:  # save only the first 3 images
            image = io.imread(link)
            filename = f"image_{idx + 1}.jpg"
            image_path = os.path.join("static", "images", filename)
            io.imsave(image_path, image)
            saved_images_paths.append(image_path)
    return saved_images_paths


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        tone = request.form['tone']
        genre = request.form['genre']
        length = int(request.form['length'])
        captions = generate_caption(topic, tone, genre, length)

        image_paths = []
        for caption in captions:
            paths = generate_images_from_prompt(caption)  # This function handles the image generation
            image_paths.extend(paths)
        # Save images locally
        saved_images = []
        for idx, link in enumerate(image_paths[:3]):
            image = io.imread(link)
            image_path = os.path.join("static", "images", f"image_{idx}.jpg")
            io.imsave(image_path, image)
            saved_images.append(image_path)

        return render_template('display.html', images=saved_images)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
