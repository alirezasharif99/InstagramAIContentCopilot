from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

input_text = "Create a catchy caption for Bayern page"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

output = model.generate(
    input_ids,
    max_length=50,
    num_return_sequences=5,
    temperature=0.7,
    do_sample=True,
    top_k=50
)

for i in range(5):
    print(tokenizer.decode(output[i], skip_special_tokens=True))

