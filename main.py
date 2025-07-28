import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_x_posts(topic: str) -> str:
    prompt = f"""
    You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).
    
    Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
    Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).
    
    Keep your post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.
    
    Here is the topic provided by the user for which you need to generate a post:
    <topic>
    {topic}
    </topic>
    """

    payload = {
        "model": "gpt-4o",
        "input": prompt
    }

    response = requests.post(
        "https://api.openai.com/v1/responses",
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        })

    response_text = response.json().get("output", [{}])[
        0].get("content", [{}])[0].get("text", "")

    return response_text


def main():
    user_input = input("What should be the post be about?")
    x_post = generate_x_posts(user_input)
    print(f"Generated X post: {x_post}")


if __name__ == "__main__":
    main()
