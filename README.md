# URL_fr_shrt

✨ Local URL Shortener + GitHub Auto Push Shortcut

This project is a local mini URL shortener server with a clean frontend, dark mode toggle, and a desktop shortcut to automatically push changes to GitHub.

It runs entirely locally on your machine, using a lightweight Python HTTP server, HTML, CSS, and JavaScript — no external services required.
📂 Features

- ✅ Local Server: A Python http.server that serves your frontend files and handles URL shortening requests.

- ✅ URL Shortening: Enter a URL, click a button, and get a shortened version back.

- ✅ Automatic Redirects: Shortened URLs redirect back to the original full URL.

- ✅ Dark Mode Toggle: Easy switch between light and dark themes.

- ✅ Background Python Server: Runs without opening a visible terminal window.

## 🚀 How It Works

    Server Side:

        Python (server.py) handles all file serving and API requests.

        It maps URLs to local files via a file_map.

        When you submit a URL, it returns a shortened URL.

        When a shortened URL is accessed, it redirects back to the original URL.

    Frontend:

        index.html has an input field with placeholder text that disappears when you type.

        style.css styles the page with dark/light mode support.

        script.js sends the URL you type to the server and updates the page with the shortened URL.

    GitHub Push Shortcut:

        A .bat or .sh script adds, commits, and pushes all changes to your GitHub repo with one click.

        Saves time during development.

🛠 Installation & Usage
1. Clone or Download the Repository

``` cmd
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Setup and Run the Server

    Run the Python server in background using a shortcut (using pythonw.exe if on Windows).

Example background shortcut:

pythonw server.py

Or simply:

python server.py

(for testing with visible console)

This will start the server at:

http://localhost:8000/

3. Frontend

    Open your browser and navigate to http://localhost:8000/.

    Enter a URL, click the shorten button, and you'll get your local shortened URL.

4. GitHub Auto Push

    Use the provided git_push.bat (Windows) or git_push.sh (Linux/macOS) script.

    Double-click the desktop shortcut to automatically:

        git add .

        git commit -m "Auto commit via shortcut"

        git push origin main

Make sure to edit the script with your repository's local path and correct branch name (main or master).
📋 Requirements

    Python 3.x

    Git

    A GitHub account with an existing repository cloned locally.

💬 Notes

    This project is for local use. Shortened links will only work while your server is running.

    Security: No authentication or validation is added — it's intended for personal, local usage.

    Customizations: Feel free to modify the server to use a database for URL storage or deploy it externally!

📸 Screenshots

    (Add your own screenshots here if you want — a screenshot of the input page in light/dark mode would look great.)

🧠 Future Ideas

    Password-protected links 🔒

    QR code generation 📷

    Database integration 🛢️

    Full deployment (e.g., using Flask + Docker)

📜 License

This project is open-source and free to use under the MIT License.
🌟 Enjoy your personal URL shortener!
