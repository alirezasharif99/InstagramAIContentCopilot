import tkinter as tk
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_caption():
    custom = custom_entry.get()

    if custom:  # If there's a custom prompt, use it
        prompt = custom
    else:  # Else, create a prompt from the user's inputs
        topic = topic_entry.get()
        tone = tone_entry.get()
        length = length_entry.get()
        prompt = f"Write a {tone} around {length} words caption about {topic}."

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    output = model.generate(
        input_ids,
        max_length=100,
        num_return_sequences=5,
        temperature=0.7,
        do_sample=True,
        top_k=50
    )

    captions = [tokenizer.decode(o[len(input_ids[0]):], skip_special_tokens=True) for o in output]
    result.set('\n\n'.join(captions))

# GUI Design
root = tk.Tk()
root.title("Caption Generator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Input Fields for Topic, Tone, Genre
labels = ['Topic:', 'Tone:', 'Length:', 'Custom Prompt:']
entries = [tk.Entry(frame) for _ in labels]

for i, label in enumerate(labels):
    tk.Label(frame, text=label).grid(row=i, column=0, sticky='w', pady=5)
    entries[i].grid(row=i, column=1, pady=5)

topic_entry, tone_entry, length_entry, custom_entry = entries

# Generate Button
generate_button = tk.Button(frame, text="Generate Captions", command=generate_caption)
generate_button.grid(row=len(labels), columnspan=2, pady=20)

# Output Area
result = tk.StringVar()
result.set("Generated captions will be displayed here.")
output_label = tk.Label(frame, textvariable=result, wraplength=500)
output_label.grid(row=len(labels) + 1, columnspan=2, pady=5)

# Running the application
root.mainloop()
