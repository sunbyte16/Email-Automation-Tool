"""
Email Automation Tool - Configuration Template
Copy this file to config.py and fill in your email settings.
"""

# Email Configuration Template
# Copy this file to config.py and update with your actual credentials

EMAIL_CONFIG = {
    # Email provider: 'gmail' or 'outlook'
    'provider': 'gmail',
    
    # Your email address
    'email': 'your_email@gmail.com',
    
    # Your app password (NOT your regular password)
    'app_password': 'your_app_password_here',
    
    # SMTP settings (usually don't need to change these)
    'smtp_server': 'smtp.gmail.com',  # or 'smtp-mail.outlook.com' for Outlook
    'smtp_port': 587
}

# Default recipient file paths
DEFAULT_RECIPIENTS_CSV = 'sample_recipients.csv'
DEFAULT_RECIPIENTS_JSON = 'sample_recipients.json'

# Email sending settings
EMAIL_SETTINGS = {
    # Delay between emails (in seconds) to avoid rate limiting
    'delay_between_emails': 1,
    
    # Maximum retry attempts for failed emails
    'max_retries': 3,
    
    # Log file path
    'log_file': 'email_logs.log'
}

# Personalization placeholders
PLACEHOLDERS = {
    'name': '{Name}',
    'email': '{Email}',
    'first_name': '{FirstName}',  # You can add more placeholders
    'last_name': '{LastName}'
}
