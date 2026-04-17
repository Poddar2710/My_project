from google import genai

client = genai.Client(api_key="your_API")

response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents="What crop is best in summer?"
)

print(response.text)
