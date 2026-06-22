import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_route_advice(
    source: str,
    destination: str,
    budget: int,
    date: str,
):

    prompt = f"""
You are an Indian Railway Travel Assistant.

Travel Details:
Source: {source}
Destination: {destination}
Budget: {budget}
Date: {date}

Provide:
1. Recommended Route
2. Alternative Route
3. Tatkal Tips
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content