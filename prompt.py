import openai

openai.api_base = 'https://ericmichael-openai-playground-utrgv.hf.space/v1'
openai.api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmODFmYzE1NS1jNGZiLTQ0MWUtYWFmNy0wMTMzYTY1NWVhMmMiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTcxNTgxNjEwNX0.RjhdJSZJMhRJlGMeUF0jiR5s2yrNHd8SPion7ISms3U"

script = """
[Phone rings, and an insurance agent answers]

Agent: Thank you for calling XYZ Insurance. This is [Agent Name]. How can I assist you today?

Caller: Yeah, this is [Patient Name]. I've been dealing with your company for weeks, and I've had enough!

Agent: I'm sorry to hear that, [Patient Name]. Can you please tell me what seems to be the issue?

Caller: The issue is that every time I try to get information about my claim, I get transferred from one department to another. It's like nobody knows what they're doing over there!

Agent: I understand your frustration, [Patient Name]. I apologize for any inconvenience. Let me pull up your file and see what's going on. Can you provide me with your policy number?

Caller: Ugh, fine. It's ABC123456.

Agent: Thank you, [Patient Name]. Please give me a moment.

[Agent puts the caller on hold for a short while]

Agent: Okay, [Patient Name], I've located your file. I see that there have been some delays in processing your claim, and I sincerely apologize for that.

Caller: Delays? It's been a nightmare! I submitted all the required documents, and I keep getting the runaround. I need this sorted out ASAP.

Agent: I completely understand, [Patient Name]. I'll escalate this issue to our claims department right away and ensure they prioritize your case. Can you provide me with any specific details or dates related to your claim?

Caller: I shouldn't have to repeat myself, but fine. It was for a medical procedure on [specific date], and the claim was submitted on [another specific date].

Agent: Thank you for the details, [Patient Name]. I'll make sure to include that information in the escalation. Please allow us some time to investigate and get back to you with a resolution.

Caller: It better be soon. I've had enough of this incompetence. If I don't see progress, I'll be taking my business elsewhere.

Agent: I completely understand your concerns, [Patient Name]. We'll do our best to address this promptly. Thank you for bringing it to our attention.

[The call concludes with the agent promising to follow up on the issue]

Note: This is a fictional and generic script, and real-life interactions may vary. It's important to approach such situations with empathy and professionalism.
"""
prompt = """In 30 words or less list all your answers, determine the reason for the call, determine the tone of the call between the caller and receiptient,
Identify the relationship between the caller and receiptient (Patient, Care-Giver, Insurance Representative, Other Medical Office, Other), Determine whether there was an issue or complain raised by the caller?,
Determine whether the call resulted in a successfully scheduled appointment? If not, what was the reason?.
"""
audio = ""

with open('C:/Users/19566/OneDrive - The University of Texas-Rio Grande Valley/Documents/Sound recordings/test1.txt', 'r') as file:
    # Read the content of the file
    file_content = file.read()

with open('C:/Users/19566/OneDrive - The University of Texas-Rio Grande Valley/Documents/Sound recordings/test2.txt', 'r') as file:
    # Read the content of the file
    file_content2 = file.read()
    
with open('C:/Users/19566/OneDrive - The University of Texas-Rio Grande Valley/Documents/Sound recordings/test3.txt', 'r') as file:
    # Read the content of the file
    file_content3 = file.read()


# print(file_content)

model="gpt-3.5-turbo"

messages=[{"role": "user", "content": prompt + file_content3}]
completion = openai.ChatCompletion.create(model=model, messages=messages)
print(completion.choices[0].message.content)

# messages=[{"role": "user", "content": prompt + script}]
# completion = openai.ChatCompletion.create(model=model, messages=messages)
# print(completion.choices[0].message.content)


