import os
from openai import OpenAI
import traceback

os.environ["OPENROUTER_API_KEY"] = (
    "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"
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def title_agent(state):
    try:
        transcript = state["transcript"]
        prompt = f"Write a catchy blog-style title for this video transcript:\n\n{transcript[:3000]}"

        print("Sending request to OpenRouter API...")
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:3000",
                "X-Title": "YouTube Blog Generator App",
            },
            model="anthropic/claude-3-opus",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100,
        )
        print("Received response from OpenRouter API")
        print(f"Response: {completion}")

        if not completion or not completion.choices:
            raise ValueError("No response received from OpenRouter API")

        return {"title": completion.choices[0].message.content}
    except Exception as e:
        print(f"Error in title_agent: {str(e)}")
        print("Full traceback:")
        print(traceback.format_exc())
        raise
