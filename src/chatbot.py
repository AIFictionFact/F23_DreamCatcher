import openai
import gradio

openai.api_key = "###"

messages = [{"role": "system", "content": "You are a dream interpreter that can decipher the meanings of peoples dreams contextualized by their personal experiences and feelings"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "DREAMCATCHER")

demo.launch(share=True)