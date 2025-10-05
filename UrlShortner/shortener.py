#!/usr/bin/env python3
"""
Local URL Shortener - CLI
Author: Joshua
"""

import json
import os

DATA_FILE = "urls.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_url():
    data = load_data()
    short = input("Enter short code (e.g. yt, gh, shop): ").strip().lower()
    if short in data:
        print("❌ This short code already exists.")
        return
    long_url = input("Enter the full URL: ").strip()
    data[short] = long_url
    save_data(data)
    print(f"✅ Saved! '{short}' → {long_url}")


def get_url():
    data = load_data()
    short = input("Enter short code to open: ").strip().lower()
    if short not in data:
        print("❌ Short code not found.")
    else:
        print(f"🔗 Full URL: {data[short]}")


def list_urls():
    data = load_data()
    if not data:
        print("No links saved yet.")
        return
    print("\n--- Saved Short Links ---")
    for k, v in data.items():
        print(f"{k:10} → {v}")
    print("-------------------------")


def delete_url():
    data = load_data()
    short = input("Enter short code to delete: ").strip().lower()
    if short in data:
        confirm = input(f"Are you sure you want to delete '{short}'? (y/n): ").lower()
        if confirm == "y":
            del data[short]
            save_data(data)
            print("✅ Deleted.")
    else:
        print("❌ Code not found.")


def menu():
    options = {
        "1": ("Add a short URL", add_url),
        "2": ("Get a full URL", get_url),
        "3": ("List all short URLs", list_urls),
        "4": ("Delete a short URL", delete_url),
    }

    while True:
        print("\n--- Local URL Shortener ---")
        for k, (desc, _) in options.items():
            print(f"{k}. {desc}")
        print("5. Quit")

        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break

        action = options.get(choice)
        if action:
            action[1]()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
