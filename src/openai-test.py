from openai import OpenAI
#from dotenv import load_dotenv
#import os

# Load environment variables from .env file
#load_dotenv()

# Retrieve the API key from the environment variables
##api_key = os.environ["OPENAI_API_KEY"]

# Initialize the OpenAI client
client = OpenAI(api_key='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')
#print(client)   


completion = client.chat.completions.create(    
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)

