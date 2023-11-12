class InteractionClassifier:
    def __init__(self):
        self.doctor_keywords = ["doctor", "check", "prescribing", "medicines", "checkup"]
        self.insurance_keywords = ["insurance", "coverage", "claim", "policy", "premium"]

    def classify_interaction(self, transcript):
        interaction_type = "Unclassified"

        for sentence in transcript:
            if any(keyword in sentence for keyword in self.doctor_keywords):
                interaction_type = "Doctor-Patient"
                break
            elif any(keyword in sentence for keyword in self.insurance_keywords):
                interaction_type = "Insurance-Patient"
                break

        return interaction_type

# Example usage with your provided transcript
transcript = [
    "Hello, I'm calling about my recent medical expenses. I wanted to check on the status of my claims.",
"Hi there! Thank you for reaching out. I'd be happy to assist you. Could you please provide me with your policy number and some basic information to access your account?",
"Sure, my policy number is ABC123456. My name is John Doe, and my date of birth is January 15, 1980.",
"Thank you, John. Let me pull up your information. (Pause) Great, I've got your details. How can I assist you with your claims?",
"I recently had a visit to the hospital, and I've submitted the necessary documents for reimbursement. I wanted to know the status of my claim and when I can expect the reimbursement.",
"I appreciate you bringing this to our attention, John. I'll check the status of your claim right away. (Pause) It looks like your claim is currently in the processing stage. Our team is reviewing the submitted documents, and we aim to complete the process within the next two weeks. You should receive a notification once the reimbursement is processed.",
"Okay, that's good to know. Is there anything else I need to do or provide to expedite the process?",
"At the moment, everything seems to be in order. However, if our team requires any additional information, we'll reach out to you promptly. In the meantime, feel free to contact us if you have any further questions or concerns.",
"Alright, thank you. Also, I wanted to inquire about the coverage for a specific prescription medication. Can you provide information on that?",
"Certainly, John. I can look up the details for you. Could you please provide the name of the medication and the dosage?",
"The medication is called HealthX, and I take it in 50mg tablets.",
"Thank you for the information. Let me check your policy coverage for HealthX. (Pause) It appears that HealthX is covered under your prescription drug benefits. You have a co-payment of $20 for a 30-day supply. Is there anything else you'd like to know about your coverage?", 
"That's all for now. Thanks for your help!",
"You're welcome, John! If you have any more questions in the future or if there's anything else we can assist you with, please don't hesitate to reach out. Have a great day!"
]

classifier = InteractionClassifier()
interaction_type = classifier.classify_interaction(transcript)

# Print the result
print(f"Interaction Type: {interaction_type}")
