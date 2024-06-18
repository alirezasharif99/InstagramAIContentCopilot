from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Function to generate captions
def generate_caption(topic, tone, genre, length):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Constructing the prompt using user inputs
    prompt = f"Write a {tone} {genre} caption about {topic} that is approximately {length} words long."

    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Adjusting max_length to be roughly the number of tokens corresponding to user's word length preference
    max_tokens = length * 5  

    output = model.generate(
        input_ids,
        max_length=max_tokens,
        num_return_sequences=5,
        temperature=0.7,
        do_sample=True,
        top_k=50
    )

    for i in range(5):
        print(tokenizer.decode(output[i], skip_special_tokens=True))

# Taking user inputs for customization
topic = input("Enter the topic: ")
tone = input("Enter the tone (e.g., humorous, inspirational, informative): ")
genre = input("Enter the genre (e.g., quote, story, fact): ")
length = int(input("Enter the approximate word length for the caption: "))

generate_caption(topic, tone, genre, length)

