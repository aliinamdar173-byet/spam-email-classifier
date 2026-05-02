# Spam Email Classifier
# Author: Inamdar Mohammad Ali

# Simple rule-based spam classifier (no external libraries needed)
# Uses keyword matching and scoring to classify emails

SPAM_KEYWORDS = [
    "free", "winner", "won", "prize", "claim", "urgent", "act now",
    "limited time", "click here", "buy now", "earn money", "make money",
    "congratulations", "selected", "offer", "discount", "deal", "cash",
    "lottery", "bitcoin", "crypto", "investment", "guaranteed", "risk free",
    "no cost", "100%", "double your", "work from home", "get paid"
]

HAM_KEYWORDS = [
    "meeting", "project", "report", "schedule", "team", "update",
    "assignment", "submission", "deadline", "review", "please", "regards",
    "attached", "document", "presentation", "feedback", "discussion"
]

def preprocess(text):
    return text.lower()

def classify_email(subject, body):
    text = preprocess(subject + " " + body)
    spam_score = 0
    ham_score = 0
    matched_spam = []
    matched_ham = []

    for keyword in SPAM_KEYWORDS:
        if keyword in text:
            spam_score += 1
            matched_spam.append(keyword)

    for keyword in HAM_KEYWORDS:
        if keyword in text:
            ham_score += 1
            matched_ham.append(keyword)

    # Classification logic
    if spam_score >= 3:
        label = "SPAM"
        confidence = min(95, 60 + (spam_score * 5))
    elif spam_score >= 1 and ham_score == 0:
        label = "SPAM"
        confidence = 55 + (spam_score * 5)
    else:
        label = "HAM (Not Spam)"
        confidence = min(95, 60 + (ham_score * 5))

    return label, confidence, matched_spam, matched_ham

def print_result(label, confidence, matched_spam, matched_ham):
    print("\n" + "=" * 45)
    print("         CLASSIFICATION RESULT")
    print("=" * 45)
    print(f"  Result     : {label}")
    print(f"  Confidence : {confidence}%")
    if matched_spam:
        print(f"  Spam words : {', '.join(matched_spam)}")
    if matched_ham:
        print(f"  Ham words  : {', '.join(matched_ham)}")
    print("=" * 45)

def run_demo():
    test_emails = [
        {
            "subject": "Congratulations! You have won a free prize!",
            "body": "Click here to claim your reward. Limited time offer. Act now and earn money fast!"
        },
        {
            "subject": "Project Update - Team Meeting Tomorrow",
            "body": "Hi team, please find attached the project report. Kindly review before our meeting. Regards."
        },
        {
            "subject": "Exclusive deal just for you",
            "body": "Buy now and get 100% discount. No cost to you. Guaranteed results!"
        },
        {
            "subject": "Assignment Submission Reminder",
            "body": "Dear student, please submit your assignment before the deadline. Feedback will be shared after review."
        }
    ]

    print("\n--- Running Demo on Sample Emails ---")
    for i, email in enumerate(test_emails, 1):
        print(f"\nEmail {i}:")
        print(f"  Subject : {email['subject']}")
        print(f"  Body    : {email['body'][:60]}...")
        label, confidence, sp, hm = classify_email(email["subject"], email["body"])
        print_result(label, confidence, sp, hm)

def main():
    print("=" * 45)
    print("       SPAM EMAIL CLASSIFIER")
    print("=" * 45)
    print("1. Classify your own email")
    print("2. Run demo on sample emails")
    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        subject = input("\nEnter email subject: ")
        body = input("Enter email body: ")
        label, confidence, sp, hm = classify_email(subject, body)
        print_result(label, confidence, sp, hm)
    elif choice == "2":
        run_demo()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
