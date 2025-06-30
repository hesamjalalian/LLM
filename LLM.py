import json
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_emails(filename="sample_emails.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def generate_reply(email_text, sender_name):
    prompt = f"{sender_name} said: {email_text}\nAI assistant reply:"
    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")

    outputs = model.generate(
        inputs,
        max_length=150,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        num_return_sequences=1,
    )

    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    reply = reply[len(prompt):].strip()

    full_reply = f"Dear {sender_name},\n\n{reply}\n\nBest regards,\nYour AI Assistant"
    return full_reply

def main():
    emails = load_emails()

    for entry in emails:
        sender = entry["sender"]
        email_text = entry["email"]

        reply = generate_reply(email_text, sender)
        print(f"\n--- Reply to {sender} ---")
        print(reply)
        print("--- End of Reply ---\n")

if __name__ == "__main__":
    main()
