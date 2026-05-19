from langchain.chat_models import init_chat_model

GOOGLE_API_KEY = "AIzaSyA6RRmQ5VMPuFa4uFRjYeUn-g82Tlf0DKo"

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY)

response = model.invoke("How is weather today in Tbilisi?")

response_str = response.content[0]['text']

print(response_str)

