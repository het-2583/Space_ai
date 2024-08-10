import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key'

def ask_space_question(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question only if it's about space technology: {question}",
        max_tokens=150,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer
