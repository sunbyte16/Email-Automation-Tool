#!/usr/bin/env python3
"""
Email Automation Tool
A comprehensive tool for sending bulk emails with personalization, attachments, and scheduling.
"""

import smtplib
import json
import csv
import os
import sys
import time
import logging
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List, Dict, Optional, Tuple
import threading
import schedule


class EmailAutomationTool:
    """Main class for email automation functionality."""
    
    def __init__(self):
        """Initialize the email automation tool."""
        self.smtp_config = {
            'gmail': {
                'smtp_server': 'smtp.gmail.com',
                'smtp_port': 587
            },
            'outlook': {
                'smtp_server': 'smtp-mail.outlook.com',
                'smtp_port': 587
            }
        }
        self.recipients = []
        self.email_config = {}
        self.setup_logging()
    
    def setup_logging(self):
        """Setup logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('email_logs.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def load_recipients(self, file_path: str) -> bool:
        """
        Load recipients from CSV or JSON file.
        
        Args:
            file_path (str): Path to the recipients file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                return False
            
            self.recipients = []
            
            if file_path.endswith('.csv'):
                with open(file_path, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if 'Name' in row and 'Email' in row:
                            self.recipients.append({
                                'name': row['Name'].strip(),
                                'email': row['Email'].strip()
                            })
                        else:
                            print("❌ CSV file must contain 'Name' and 'Email' columns")
                            return False
            
            elif file_path.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        for recipient in data:
                            if 'name' in recipient and 'email' in recipient:
                                self.recipients.append({
                                    'name': recipient['name'].strip(),
                                    'email': recipient['email'].strip()
                                })
                            else:
                                print("❌ JSON file must contain 'name' and 'email' fields")
                                return False
                    else:
                        print("❌ JSON file must contain a list of recipients")
                        return False
            
            else:
                print("❌ Unsupported file format. Please use CSV or JSON files.")
                return False
            
            print(f"✅ Successfully loaded {len(self.recipients)} recipients")
            self.logger.info(f"Loaded {len(self.recipients)} recipients from {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading recipients: {str(e)}")
            self.logger.error(f"Error loading recipients: {str(e)}")
            return False
    
    def configure_email(self) -> bool:
        """
        Configure email settings for SMTP.
        
        Returns:
            bool: True if successful, False otherwise
        """
        print("\n📧 Email Configuration")
        print("=" * 50)
        
        # Select email provider
        print("Select email provider:")
        print("1. Gmail")
        print("2. Outlook")
        
        while True:
            choice = input("Enter choice (1-2): ").strip()
            if choice == '1':
                provider = 'gmail'
                break
            elif choice == '2':
                provider = 'outlook'
                break
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
        
        # Get email credentials
        email = input("Enter your email address: ").strip()
        app_password = input("Enter your app password: ").strip()
        
        if not email or not app_password:
            print("❌ Email and app password are required")
            return False
        
        self.email_config = {
            'provider': provider,
            'email': email,
            'password': app_password,
            'smtp_server': self.smtp_config[provider]['smtp_server'],
            'smtp_port': self.smtp_config[provider]['smtp_port']
        }
        
        # Test connection
        if self.test_smtp_connection():
            print("✅ Email configuration successful!")
            self.logger.info(f"Email configured for {email}")
            return True
        else:
            print("❌ Failed to connect to SMTP server")
            return False
    
    def test_smtp_connection(self) -> bool:
        """
        Test SMTP connection with provided credentials.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['email'], self.email_config['password'])
            server.quit()
            return True
        except Exception as e:
            self.logger.error(f"SMTP connection test failed: {str(e)}")
            return False
    
    def compose_email(self) -> Dict[str, str]:
        """
        Compose email with subject and body.
        
        Returns:
            Dict[str, str]: Email composition data
        """
        print("\n✍️ Compose Email")
        print("=" * 50)
        
        subject = input("Enter email subject: ").strip()
        if not subject:
            print("❌ Subject cannot be empty")
            return {}
        
        print("\nSelect email format:")
        print("1. Plain Text")
        print("2. HTML")
        
        while True:
            format_choice = input("Enter choice (1-2): ").strip()
            if format_choice == '1':
                email_format = 'plain'
                break
            elif format_choice == '2':
                email_format = 'html'
                break
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
        
        print(f"\nEnter email body ({email_format} format):")
        print("Use {Name} for personalization (e.g., Hello {Name}!)")
        print("Press Ctrl+Z (Windows) or Ctrl+D (Mac/Linux) when finished:")
        
        body_lines = []
        try:
            while True:
                line = input()
                body_lines.append(line)
        except EOFError:
            pass
        
        body = '\n'.join(body_lines)
        if not body.strip():
            print("❌ Email body cannot be empty")
            return {}
        
        # Ask for attachments
        attachments = []
        while True:
            attach = input("\nAdd attachment? (y/n): ").strip().lower()
            if attach == 'n':
                break
            elif attach == 'y':
                file_path = input("Enter file path: ").strip()
                if os.path.exists(file_path):
                    attachments.append(file_path)
                    print(f"✅ Added attachment: {os.path.basename(file_path)}")
                else:
                    print("❌ File not found")
            else:
                print("❌ Please enter 'y' or 'n'")
        
        return {
            'subject': subject,
            'body': body,
            'format': email_format,
            'attachments': attachments
        }
    
    def personalize_message(self, message: str, recipient: Dict[str, str]) -> str:
        """
        Personalize message with recipient data.
        
        Args:
            message (str): Original message
            recipient (Dict[str, str]): Recipient data
            
        Returns:
            str: Personalized message
        """
        personalized = message.replace('{Name}', recipient['name'])
        personalized = personalized.replace('{Email}', recipient['email'])
        return personalized
    
    def create_email_message(self, recipient: Dict[str, str], email_data: Dict[str, str]) -> MIMEMultipart:
        """
        Create email message with personalization and attachments.
        
        Args:
            recipient (Dict[str, str]): Recipient data
            email_data (Dict[str, str]): Email composition data
            
        Returns:
            MIMEMultipart: Email message object
        """
        msg = MIMEMultipart()
        msg['From'] = self.email_config['email']
        msg['To'] = recipient['email']
        msg['Subject'] = email_data['subject']
        
        # Personalize body
        personalized_body = self.personalize_message(email_data['body'], recipient)
        
        # Add body
        if email_data['format'] == 'html':
            msg.attach(MIMEText(personalized_body, 'html'))
        else:
            msg.attach(MIMEText(personalized_body, 'plain'))
        
        # Add attachments
        for attachment_path in email_data['attachments']:
            try:
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {os.path.basename(attachment_path)}'
                    )
                    msg.attach(part)
            except Exception as e:
                self.logger.error(f"Failed to attach {attachment_path}: {str(e)}")
        
        return msg
    
    def send_email(self, recipient: Dict[str, str], email_data: Dict[str, str]) -> Tuple[bool, str]:
        """
        Send email to a single recipient.
        
        Args:
            recipient (Dict[str, str]): Recipient data
            email_data (Dict[str, str]): Email composition data
            
        Returns:
            Tuple[bool, str]: Success status and message
        """
        try:
            # Create email message
            msg = self.create_email_message(recipient, email_data)
            
            # Connect to SMTP server
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['email'], self.email_config['password'])
            
            # Send email
            text = msg.as_string()
            server.sendmail(self.email_config['email'], recipient['email'], text)
            server.quit()
            
            success_msg = f"Email sent successfully to {recipient['name']} ({recipient['email']})"
            self.logger.info(success_msg)
            return True, success_msg
            
        except Exception as e:
            error_msg = f"Failed to send email to {recipient['name']} ({recipient['email']}): {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg
    
    def send_bulk_emails(self, email_data: Dict[str, str]) -> None:
        """
        Send bulk emails to all recipients.
        
        Args:
            email_data (Dict[str, str]): Email composition data
        """
        if not self.recipients:
            print("❌ No recipients loaded. Please load recipients first.")
            return
        
        if not self.email_config:
            print("❌ Email not configured. Please configure email first.")
            return
        
        print(f"\n📤 Sending emails to {len(self.recipients)} recipients...")
        print("=" * 50)
        
        successful = 0
        failed = 0
        
        for i, recipient in enumerate(self.recipients, 1):
            print(f"[{i}/{len(self.recipients)}] Sending to {recipient['name']}...")
            
            success, message = self.send_email(recipient, email_data)
            
            if success:
                print(f"✅ {message}")
                successful += 1
            else:
                print(f"❌ {message}")
                failed += 1
            
            # Add delay to avoid rate limiting
            time.sleep(1)
        
        print(f"\n📊 Summary:")
        print(f"✅ Successful: {successful}")
        print(f"❌ Failed: {failed}")
        print(f"📝 Total: {len(self.recipients)}")
        
        self.logger.info(f"Bulk email completed: {successful} successful, {failed} failed")
    
    def preview_email(self, email_data: Dict[str, str]) -> None:
        """
        Preview email for the first recipient.
        
        Args:
            email_data (Dict[str, str]): Email composition data
        """
        if not self.recipients:
            print("❌ No recipients loaded.")
            return
        
        print("\n👀 Email Preview")
        print("=" * 50)
        print(f"To: {self.recipients[0]['name']} ({self.recipients[0]['email']})")
        print(f"Subject: {email_data['subject']}")
        print(f"Format: {email_data['format'].upper()}")
        print("\nBody:")
        print("-" * 30)
        preview_body = self.personalize_message(email_data['body'], self.recipients[0])
        print(preview_body)
        print("-" * 30)
        
        if email_data['attachments']:
            print(f"\nAttachments: {', '.join([os.path.basename(f) for f in email_data['attachments']])}")
    
    def schedule_email(self, email_data: Dict[str, str], delay_minutes: int) -> None:
        """
        Schedule email to be sent after specified delay.
        
        Args:
            email_data (Dict[str, str]): Email composition data
            delay_minutes (int): Delay in minutes
        """
        print(f"\n⏰ Scheduling email to be sent in {delay_minutes} minutes...")
        
        def send_scheduled():
            self.send_bulk_emails(email_data)
        
        schedule_time = datetime.now() + timedelta(minutes=delay_minutes)
        schedule.every().day.at(schedule_time.strftime("%H:%M")).do(send_scheduled)
        
        print(f"📅 Email scheduled for {schedule_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("⏳ Waiting for scheduled time... (Press Ctrl+C to cancel)")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n❌ Email scheduling cancelled.")
            schedule.clear()
    
    def show_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "=" * 60)
        print("📧 EMAIL AUTOMATION TOOL")
        print("=" * 60)
        print("1. Load Recipients (CSV/JSON)")
        print("2. Configure Email Settings")
        print("3. Compose Email")
        print("4. Preview Email")
        print("5. Send Bulk Emails")
        print("6. Schedule Email")
        print("7. View Email Logs")
        print("8. Exit")
        print("=" * 60)
    
    def view_logs(self) -> None:
        """Display recent email logs."""
        print("\n📋 Recent Email Logs")
        print("=" * 50)
        
        try:
            with open('email_logs.log', 'r') as file:
                lines = file.readlines()
                # Show last 20 lines
                recent_lines = lines[-20:] if len(lines) > 20 else lines
                for line in recent_lines:
                    print(line.strip())
        except FileNotFoundError:
            print("No logs found.")
    
    def run(self) -> None:
        """Run the main application loop."""
        print("🚀 Welcome to Email Automation Tool!")
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                file_path = input("Enter path to recipients file (CSV/JSON): ").strip()
                self.load_recipients(file_path)
            
            elif choice == '2':
                self.configure_email()
            
            elif choice == '3':
                email_data = self.compose_email()
                if email_data:
                    print("✅ Email composed successfully!")
            
            elif choice == '4':
                if not hasattr(self, '_current_email_data'):
                    print("❌ No email composed yet. Please compose an email first.")
                    continue
                self.preview_email(self._current_email_data)
            
            elif choice == '5':
                if not hasattr(self, '_current_email_data'):
                    print("❌ No email composed yet. Please compose an email first.")
                    continue
                confirm = input("Are you sure you want to send bulk emails? (y/n): ").strip().lower()
                if confirm == 'y':
                    self.send_bulk_emails(self._current_email_data)
                else:
                    print("❌ Bulk email cancelled.")
            
            elif choice == '6':
                if not hasattr(self, '_current_email_data'):
                    print("❌ No email composed yet. Please compose an email first.")
                    continue
                try:
                    delay = int(input("Enter delay in minutes: ").strip())
                    if delay > 0:
                        self.schedule_email(self._current_email_data, delay)
                    else:
                        print("❌ Delay must be positive.")
                except ValueError:
                    print("❌ Invalid delay. Please enter a number.")
            
            elif choice == '7':
                self.view_logs()
            
            elif choice == '8':
                print("👋 Thank you for using Email Automation Tool!")
                break
            
            else:
                print("❌ Invalid choice. Please enter 1-8.")
            
            # Store composed email data for reuse
            if choice == '3' and 'email_data' in locals():
                self._current_email_data = email_data
            
            input("\nPress Enter to continue...")


def main():
    """Main function to run the application."""
    try:
        tool = EmailAutomationTool()
        tool.run()
    except KeyboardInterrupt:
        print("\n\n👋 Application terminated by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        logging.error(f"Application error: {str(e)}")


if __name__ == "__main__":
    main()
