# URL-shortlist
Here’s a clean and professional README.md for your Local URL Shortener project 👇

🧩 Local URL Shortlist (CLI)

A simple command-line URL shortlist built with Python.
It stores your favorite links locally in a JSON file and lets you create easy-to-remember short codes like:

yt  →  https://youtube.com
gh  →  https://github.com


No database. No internet. Just your links.

🚀 Features

✅ Add new short links
✅ Retrieve full URLs by short code
✅ List all saved short links
✅ Delete unwanted entries
✅ Data saved persistently in urls.json
✅ Works completely offline

🧱 Requirements

Python 3.7+

No external dependencies

⚙️ Installation

Clone or download the repository:

git clone https://github.com/yourusername/url-shortener.git
cd url-shortener


Run the script:

python shortener.py

💡 Usage
▶️ Menu Options
--- Local URL Shortener ---
1. Add a short URL
2. Get a full URL
3. List all short URLs
4. Delete a short URL
5. Quit

Example:
Choose an option: 1
Enter short code: yt
Enter the full URL: https://youtube.com
✅ Saved! 'yt' → https://youtube.com

Choose an option: 3
--- Saved Short Links ---
yt         → https://youtube.com

📁 Data Storage

All data is saved in a local JSON file:

{
  "yt": "https://youtube.com",
  "gh": "https://github.com"
}


You can manually back this file up or share it between devices.

🧠 Future Ideas

 Auto-open links in browser (webbrowser module)

 Export/Import URLs as CSV

 Password protection for deletion

 Custom colorized CLI using colorama

👤 Author

Joshua
Made with ❤️ in Python.
