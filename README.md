readme_content = """# 📧 M365 Bulk Emailer

This Python script automates the process of sending HTML-formatted emails in bulk via Microsoft 365 (Graph API). Ideal for sending newsletters, event updates, or organizational announcements.

---

## Features

- Sends HTML emails to multiple recipients using M365 Graph API
- Credentials are secured via environment variables
- Reads contact list from CSV
- Supports optional BCC
- Uses an external HTML file for email content
- Minimal dependencies, no Exchange Online license required

---

## File Structure

```text
.
├── m365-bulk-emailer.py      # Main script
├── email_body.html           # Editable HTML template used as the email body
├── emaillist.csv                  # CSV file with recipient data
├── .env                      # (Optional) Local environment variable file
└── README.md                 # This file
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/jasonpit/m365-bulk-eMailer.git
cd m365-bulk-eMailer
```

### 2. Create an `.env` file

Before creating this file, you must register an application in Azure Active Directory to get the necessary credentials.

#### Steps to Create Azure App Registration:

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to **Azure Active Directory > App registrations > New registration**
3. Name the app (e.g., "M365 Bulk Emailer")
4. Choose "Single tenant" for most cases
5. Redirect URI is not required for this script (leave it blank or use `http://localhost`)
6. Click **Register**
7. Once registered, note the following values:
   - **Application (client) ID** → use for `M365_CLIENT_ID`
   - **Directory (tenant) ID** → use for `M365_TENANT_ID`
8. Under **Certificates & secrets**, create a **New client secret**
   - Copy the value (it will not be shown again) → use for `M365_CLIENT_SECRET`
9. Under **API permissions**, click **Add a permission**
   - Choose **Microsoft Graph** > **Application permissions**
   - Add `Mail.Send`
   - Click **Grant admin consent**

#### Create the `.env` file

Now that you have the required values, create a `.env` file in the project root:

```ini
M365_CLIENT_ID=your-client-id
M365_CLIENT_SECRET=your-client-secret
M365_TENANT_ID=your-tenant-id
M365_SENDER_EMAIL=your-sender@yourdomain.com
M365_BCC_EMAIL=optional-bcc@yourdomain.com
```

> This file is excluded by `.gitignore` to keep your credentials secure.

### 3. Install dependencies

```bash
pip install requests pandas python-dotenv
```

### 4. Prepare your CSV

The script expects a file named `test.csv` like this:

```csv
email
recipient1@example.com
recipient2@example.com
```

### 5. Add your HTML body

Create a file named `email_body.html` with the content you want to send. You can use standard HTML tags.

---

## 🚀 Run the Script

```bash
python m365-bulk-emailer.py
```

The script will:
- Load environment variables
- Read email content from `email_body.html`
- Parse recipient emails from `test.csv`
- Send emails one by one using the Microsoft Graph API

---

## How It Works

1. **Access Token**: Authenticates with Microsoft using the Client Credentials Flow.
2. **Reads HTML**: Loads your email content.
3. **Sends Loop**: Iterates over the recipient list and fires POST requests to the Graph API.

---

## Security Notes

- Avoid hardcoding secrets.
- Use `.env` or CI/CD secrets management.
- Do not check in real email lists to public repos.

---

## To Do / Ideas

- Retry logic on failure
- Email tracking or logging
- Rate limiting or throttling
- HTML template support with Jinja2
- GUI for non-technical users

---

## License

MIT License. See `LICENSE` for details.

---

## Author

Jason Pittman  
[GitHub](https://github.com/jasonpit) | [LinkedIn](https://linkedin.com/in/jason-pittman)
"""

# Save README.md to the repo directory
readme_path = Path("/mnt/data/README.md")
readme_path.write_text(readme_content)

readme_path.name  # Show the filename so the user can download it if needed