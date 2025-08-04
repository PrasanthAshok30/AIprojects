import openai
import os

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Store your API key in .env or as environment variable

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat_with_gpt(user_input)
        print("Bot:", response)
