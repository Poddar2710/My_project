from google import genai

client = genai.Client(api_key="AIzaSyBr0IWbS_ApWXPoZYnOGV4lo7OStHpC0vk")

response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents="What crop is best in summer?"
)

print(response.text)