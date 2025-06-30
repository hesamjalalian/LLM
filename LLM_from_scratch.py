import json

def load_emails(filename="sample_emails.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_reply(email_text, sender_name):
  
    if "price" in email_text.lower() or "support" in email_text.lower():
        body = "Thank you for your interest. I'd be happy to provide more details about pricing and support."
    elif "not loading" in email_text.lower() or "bug" in email_text.lower():
        body = "Sorry for the inconvenience. We're looking into the issue and will resolve it shortly."
    elif "thank" in email_text.lower():
        body = "You're very welcome! We're glad to hear that."
    elif "cancel" in email_text.lower():
        body = "Your cancellation request has been processed."
    elif "subscribe" in email_text.lower() or "upgrade" in email_text.lower():
        body = "We offer several subscription plans. I’ll send you more details shortly."
    elif "discount" in email_text.lower():
        body = "Yes, we offer discounts. I’ll provide you the latest options."
    elif "delivery" in email_text.lower():
        body = "I'll check the delivery schedule and get back to you."
    elif "webinar" in email_text.lower() or "register" in email_text.lower():
        body = "You can register through our website. I’ll share the link."
    elif "integrate" in email_text.lower() or "zapier" in email_text.lower():
        body = "Yes, we support integration with Zapier and other tools."
    else:
        body = "Thank you for your email. We'll get back to you shortly."

    reply = f"Dear {sender_name},\n\n{body}\n\nBest regards,\nYour AI Assistant"
    return reply

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
