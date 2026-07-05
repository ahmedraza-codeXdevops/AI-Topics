spam_numbers = {
    "9876543210",
    "9999999999",
    "8888888888",
    "7777777777"
}

print("=" * 40)
print("Scam Call Detector")
print("=" * 40)

while True:

    number = input("\nEnter Mobile Number: ")

    if number.lower() == "exit":
        break

    if number in spam_numbers:
        print("🚨 Spam Number")
    else:
        print("✅ No Spam Record Found")