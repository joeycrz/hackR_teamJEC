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
    "Good Morning, doctor. May I come in?",
    "Good Morning. How are you? You do look quite pale this morning.",
    "Yes, doctor. I’ve not been feeling well for the past few days. I’ve been having a stomach ache for a few days and feeling a bit dizzy since yesterday.",
    "Okay, let me check. (applies pressure on the stomach and checks for pain) Does it hurt here?",
    "Yes, doctor, the pain there is the sharpest.",
    "Well, you are suffering from a stomach infection, that’s the reason you are having a stomach ache and also getting dizzy. Did you change your diet recently or have something unhealthy?",
    "Actually, I went to a fair last week and ate food from the stalls there.",
    "Okay, so you are probably suffering from food poisoning. Since the food stalls in fairs are quite unhygienic, there’s a high chance those uncovered food might have caused food poisoning.",
    "I think I will never eat from any unhygienic place in the future.",
    "That’s good. I’m prescribing some medicines, have them for one week and come back for a checkup next week. And please try to avoid spicy and fried foods for now.",
    "Okay, doctor, thank you.",
    "Welcome."
]

classifier = InteractionClassifier()
interaction_type = classifier.classify_interaction(transcript)

# Print the result
print(f"Interaction Type: {interaction_type}")
