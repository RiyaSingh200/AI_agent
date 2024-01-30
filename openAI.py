import openai
from config import apikey

# Set your API key
openai.api_key = apikey

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "write an application for holiday leave "
        },
        {
            "role": "user",
            "content": ""
        },
        {
            "role": "assistant",
            "content": "[Your Name]\n[Your Address]\n[City, State, ZIP Code]\n[Email Address]\n[Phone Number]\n[Date]\n\n[Recipient's Name]\n[Recipient's Position]\n[Company/Organization Name]\n[Company/Organization Address]\n[City, State, ZIP Code]\n\nSubject: Application for Holiday Leave\n\nDear [Recipient's Name],\n\nI hope this letter finds you in good health and high spirits. I am writing to formally request holiday leave from [start date] to [end date]. I have thoroughly considered the timing and have made the necessary arrangements to ensure a seamless workflow during my absence.\n\nThe reason for my leave request is to celebrate the festive holiday season with my family and loved ones. It is a time of importance and significance to us, and I believe that taking this time off will not only allow me to recharge and rejuvenate but also enhance my productivity upon my return.\n\nDuring my absence, I have already discussed and coordinated with my colleagues and team members to ensure that there will be minimal disruption to our work processes. I am confident that they will be able to handle any urgent matters that may arise, and I will be readily available via email or phone if any exceptional situations require my attention.\n\nI understand that my leave request coincides with a busy period"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Process the response as needed
print(response)



