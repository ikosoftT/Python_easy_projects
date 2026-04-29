import requests

FAKER_URL = "https://fakerapi.it/api/v2/persons?_quantity=1000&_locale=en_GB"
OUTPUT_FILE = "emails.txt"


# -----------------------------
# Fetch data
# -----------------------------
def fetch_data():
    try:
        res = requests.get(FAKER_URL, timeout=200)
        res.raise_for_status()
        return res.json().get("data", [])
    except Exception as e:
        print("Fetch error:", e)
        return []


# -----------------------------
# Extract gmail only
# -----------------------------
def extract_gmail(persons):
    emails = []

    for p in persons:
        email = p.get("email", "")
        if email.endswith("@gmail.com"):
            emails.append(email.lower())

    return list(set(emails))  # remove duplicates


# -----------------------------
# Save to file
# -----------------------------
def save_to_file(emails):
    try:
        with open(OUTPUT_FILE, "a") as f:
            for email in emails:
                f.write(email + "\n")
    except Exception as e:
        print("File write error:", e)


# -----------------------------
# MAIN
# -----------------------------
def main():
    persons = fetch_data()

    gmail_emails = extract_gmail(persons)

    print(f"Total gmail emails found: {len(gmail_emails)}")

    save_to_file(gmail_emails)

    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
