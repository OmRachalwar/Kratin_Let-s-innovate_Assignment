import openai
openai.api_key = "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"
complete = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "When do I have to take my medicine"},
        {"role": "assistant", "content": "After Lunch and After Dinner"},
        {"role": "user", "content": "Name of the medicine After lunch"}
    ]
)
message = complete.choices[0].message.content
