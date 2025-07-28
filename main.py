import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def generate_x_posts(topic: str) -> str:
    with open("post-examples.json", "r") as f:
        examples = json.load(f)

    examples_str = ""
    for i, example in enumerate(examples, 1):
        examples_str += f"""
        <example-{i}>
            <topic>
            {example['topic']}
            </topic>

            <generated-post>
            {example['post']}
            </generated-post>
        </example-{i}>
        """

    prompt = f"""
    You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).
    
    Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
    Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).
    
    Keep your post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.
    
    Here is the topic provided by the user for which you need to generate a post:
    <topic>
        {topic}
    </topic>
    
    Here are some examples of topics and generated posts:
    <examples>
        {examples_str}
    </examples>
    """

    response = client.responses.create(
        model="gpt-4o",
        input=prompt,
    )

    return response.output_text


def main():
    user_input = input("What should be the post be about?")
    x_post = generate_x_posts(user_input)
    print(f"Generated X post: {x_post}")


if __name__ == "__main__":
    main()
