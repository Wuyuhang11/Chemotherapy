from huggingface_hub import InferenceClient

client = InferenceClient(api_key="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")

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions.create(
    model="meta-llama/Llama-2-7b-chat-hf", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message)