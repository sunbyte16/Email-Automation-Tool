# 📧 Email Automation Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)

**A comprehensive Python tool for sending bulk emails with personalization, attachments, and scheduling capabilities.**

[![GitHub](https://img.shields.io/badge/GitHub-@sunbyte16-black?style=social&logo=github)](https://github.com/sunbyte16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sunil%20Kumar-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/sunil-kumar-bb88bb31a/)
[![Portfolio](https://img.shields.io/badge/Portfolio-View%20Live-orange?style=social&logo=netlify)](https://lively-dodol-cc397c.netlify.app)

---

**This is Crafted By [Sharma Ji❤️](https://github.com/sunbyte16)**

</div>

## ✨ Features

<div align="center">

| 🚀 **Core Features** | 📊 **Advanced Features** | 🛡️ **Security & Quality** |
|:---:|:---:|:---:|
| 📧 Bulk Email Sending | ⏰ Email Scheduling | 🔐 App Password Auth |
| 🎯 Personalization | 📎 Attachment Support | 🔒 TLS Encryption |
| 📱 Multi-Provider | 📋 Data Import (CSV/JSON) | ✅ Input Validation |
| 🎨 HTML & Plain Text | 👀 Email Preview | 📝 Comprehensive Logging |
| 🌐 Gmail & Outlook | 📊 Delivery Tracking | 🚨 Error Handling |

</div>

### 🎯 **Key Capabilities**

- **📧 Bulk Email Sending**: Send personalized emails to multiple recipients simultaneously
- **🎭 Personalization**: Use smart placeholders like `{Name}` and `{Email}` in your messages
- **🌐 Multi-Provider Support**: Seamless integration with Gmail and Outlook SMTP
- **📎 Attachment Support**: Send any file type (PDF, images, documents) with your emails
- **⏰ Email Scheduling**: Schedule emails to be sent at a later time with precision
- **🎨 Multiple Formats**: Support for both plain text and rich HTML email formats
- **📊 Comprehensive Logging**: Track email delivery status, success rates, and errors
- **📋 Data Import**: Load recipients from CSV or JSON files with validation
- **👀 Email Preview**: Preview personalized emails before sending
- **🛡️ Robust Error Handling**: Comprehensive validation and error management

## 🚀 Quick Start

<div align="center">

### ⚡ **Get Started in 3 Steps!**

| Step | Action | Command |
|:---:|:---:|:---:|
| 1️⃣ | **Clone Repository** | `git clone https://github.com/sunbyte16/email-automation-tool.git` |
| 2️⃣ | **Install Dependencies** | `pip install -r requirements.txt` |
| 3️⃣ | **Run Application** | `python email_automation_tool.py` |

</div>

### 📋 **Prerequisites**

- 🐍 **Python 3.7+** - [Download Python](https://python.org/downloads/)
- 📧 **Email Account** - Gmail or Outlook with app password enabled
- 💻 **Operating System** - Windows, macOS, or Linux

### 🛠️ **Installation Guide**

<details>
<summary><b>📥 Step-by-Step Installation</b></summary>

#### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/sunbyte16/email-automation-tool.git
cd email-automation-tool
```

#### 2️⃣ **Install Dependencies**
```bash
# Install required packages
pip install -r requirements.txt

# Or install manually
pip install schedule==1.2.0
```

#### 3️⃣ **Run the Application**
```bash
# Method 1: Python command
python email_automation_tool.py

# Method 2: Windows batch file (double-click)
run_email_tool.bat
```

</details>

## 📋 Setup Instructions

### 🔐 **Email Configuration**

<div align="center">

| Provider | Steps | Security |
|:---:|:---:|:---:|
| 📧 **Gmail** | 2FA → App Password | 🔒 High |
| 📧 **Outlook** | 2FA → App Password | 🔒 High |

</div>

<details>
<summary><b>📧 Gmail Setup Guide</b></summary>

#### 🔑 **Step 1: Enable 2-Factor Authentication**
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Click on **2-Step Verification**
3. Follow the setup process

#### 🔐 **Step 2: Generate App Password**
1. In Google Account Security, click **App passwords**
2. Select **Mail** as the app
3. Copy the generated 16-character password
4. Use this password (not your regular password) in the tool

#### ✅ **Step 3: Configure in Tool**
- **Email**: Your Gmail address
- **Password**: The 16-character app password
- **Provider**: Gmail

</details>

<details>
<summary><b>📧 Outlook Setup Guide</b></summary>

#### 🔑 **Step 1: Enable 2-Factor Authentication**
1. Go to [Microsoft Account Security](https://account.microsoft.com/security)
2. Click on **Advanced security options**
3. Enable **Two-step verification**

#### 🔐 **Step 2: Generate App Password**
1. In Advanced security options, click **App passwords**
2. Select **Mail** as the app
3. Copy the generated password
4. Use this password in the tool

#### ✅ **Step 3: Configure in Tool**
- **Email**: Your Outlook email address
- **Password**: The generated app password
- **Provider**: Outlook

</details>

### 📊 **Prepare Recipients Data**

<div align="center">

| Format | File | Use Case |
|:---:|:---:|:---:|
| 📄 **CSV** | `sample_recipients.csv` | Excel/Google Sheets export |
| 📋 **JSON** | `sample_recipients.json` | API/Web applications |

</div>

<details>
<summary><b>📄 CSV Format Example</b></summary>

```csv
Name,Email
Sunil Sharma,sunil.shar@gmail.com
Ajay Sharma,ajay.shar@gmail.com
Raju Sharma,raju.sharma@gmail.com
Pihu Sharma,pihu.sharma@gmail.com
```

**✅ Perfect for:**
- Excel exports
- Google Sheets
- Database exports
- Bulk data management

</details>

<details>
<summary><b>📋 JSON Format Example</b></summary>

```json
[
  {
    "name": "Sunil Sharma",
    "email": "sunil.shar@gmail.com"
  },
  {
    "name": "Ajay Sharma",
    "email": "ajay.shar@gmail.com"
  },
  {
    "name": "Raju Sharma",
    "email": "raju.sharma@gmail.com"
  }
]
```

**✅ Perfect for:**
- API responses
- Web applications
- Complex data structures
- Programmatic generation

</details>

## 🎯 Usage Guide

### Main Menu Options

1. **Load Recipients (CSV/JSON)**
   - Load recipient data from a CSV or JSON file
   - Supports `Name` and `Email` fields

2. **Configure Email Settings**
   - Set up SMTP credentials for Gmail or Outlook
   - Test connection before proceeding

3. **Compose Email**
   - Create email subject and body
   - Choose between plain text or HTML format
   - Add attachments if needed
   - Use `{Name}` and `{Email}` for personalization

4. **Preview Email**
   - Preview how the email will look for the first recipient
   - Check personalization and formatting

5. **Send Bulk Emails**
   - Send emails to all loaded recipients
   - View real-time progress and results

6. **Schedule Email**
   - Schedule emails to be sent after a specified delay
   - Useful for time-sensitive campaigns

7. **View Email Logs**
   - Check recent email sending activity
   - Review success/failure status

8. **Exit Program**
   - Safely exit the application

### Personalization Examples

Use these placeholders in your email body:

- `{Name}` - Replaced with recipient's name
- `{Email}` - Replaced with recipient's email

**Example:**
```
Subject: Welcome {Name}!

Body:
Dear {Name},

Thank you for joining us! Your email {Email} has been registered.

Best regards,
The Team
```

## 📁 File Structure

```
email-automation-tool/
├── email_automation_tool.py    # Main application
├── requirements.txt            # Python dependencies
├── sample_recipients.csv      # Sample CSV recipients
├── sample_recipients.json     # Sample JSON recipients
├── sample_email_template.txt  # Email template examples
├── email_logs.log            # Email sending logs (created automatically)
└── README.md                 # This file
```

## 🔧 Configuration

### SMTP Settings

The tool supports these SMTP configurations:

- **Gmail**: smtp.gmail.com:587
- **Outlook**: smtp-mail.outlook.com:587

### Logging

All email activities are logged to `email_logs.log` with timestamps and status information.

## 🛡️ Security Features

- **App Password Authentication**: Uses app passwords instead of regular passwords
- **SMTP Security**: Uses TLS encryption for email transmission
- **Input Validation**: Validates email addresses and file formats
- **Error Handling**: Comprehensive error handling and logging

## 📊 Features in Detail

### Email Personalization
- Dynamic content replacement using placeholders
- Support for multiple personalization fields
- Preview functionality to verify personalization

### Attachment Support
- Support for any file type (PDF, images, documents)
- Automatic MIME type detection
- Error handling for missing or corrupted files

### Scheduling
- Schedule emails with minute-level precision
- Background processing with cancellation support
- Visual countdown and status updates

### Logging and Monitoring
- Detailed logs for each email sent
- Success/failure tracking
- Error message logging
- Real-time progress updates

## 🚨 Troubleshooting

### Common Issues

1. **SMTP Authentication Failed**
   - Verify your app password is correct
   - Ensure 2FA is enabled on your account
   - Check if "Less secure app access" is disabled

2. **File Not Found Errors**
   - Verify file paths are correct
   - Check file permissions
   - Ensure files exist before loading

3. **Email Delivery Issues**
   - Check recipient email addresses are valid
   - Verify SMTP server settings
   - Check for rate limiting

4. **Attachment Errors**
   - Ensure attachment files exist
   - Check file permissions
   - Verify file is not corrupted

### Getting Help

- Check the `email_logs.log` file for detailed error messages
- Verify all prerequisites are met
- Test with a small recipient list first

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📞 Support

For support or questions, please check the troubleshooting section or create an issue in the project repository.

---

<div align="center">

## 🎉 **Happy Email Automation!** 📧✨

**Created By [Sunil Sharma❤️](https://github.com/sunbyte16)**

[![GitHub](https://img.shields.io/badge/GitHub-@sunbyte16-black?style=social&logo=github)](https://github.com/sunbyte16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sunil%20Kumar-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/sunil-kumar-bb88bb31a/)
[![Portfolio](https://img.shields.io/badge/Portfolio-View%20Live-orange?style=social&logo=netlify)](https://lively-dodol-cc397c.netlify.app)

---

### 🌟 **Star this repository if you found it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/sunbyte16/email-automation-tool?style=social)](https://github.com/sunbyte16/email-automation-tool)
[![GitHub forks](https://img.shields.io/github/forks/sunbyte16/email-automation-tool?style=social)](https://github.com/sunbyte16/email-automation-tool)

</div>
