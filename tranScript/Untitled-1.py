def insert_quotation_marks(text):
    lines = text.split('\n')
    formatted_lines = ['"' + line.strip() + '"' for line in lines if line.strip()]

    formatted_text = '\n'.join(formatted_lines)
    return formatted_text

input_text = """
Good afternoon, Doctor.

Good afternoon, Mr. Bose. How are you?

I’m doing good, doctor, but my daughter isn’t doing well. Everywhere, people are getting affected with COVID and I am really worried about her.

Please have a seat and tell me what happened.

Last week, my daughter came back from Pune as her college was closed on account of COVID. From the second day, she has had high fever and has been coughing badly. I think that she has contracted the virus on her way home.

Okay, I understand your concern. Having a fever and cough doesn’t necessarily mean that someone has contracted the virus. These are symptoms of common cold too. The change in the temperature of the atmosphere could have triggered these symptoms. Still, to put your worries to rest, I am prescribing some medicines and an RT PCR test. Do the test by tomorrow, and if the test results are positive, make sure she is isolated. On the other hand, if the result is negative, just give her the medicine and ask her to drink a lot of water. Also, bring her in so I could examine her.

Okay, doctor. I will bring her in the evening. Thank you.

You are welcome.
"""

formatted_text = insert_quotation_marks(input_text)
print(formatted_text)
