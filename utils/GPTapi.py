import openai

openai.api_key =("YOUR_OPENAI_API_KEY_HERE")
def gptapi (message):
    if message == " #ERROR":
        return "Siz so'z yoki kalit so'zni yozib yuboring!"
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return (completion.choices[0].message.content)
