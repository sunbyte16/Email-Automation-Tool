#!/usr/bin/env python3
"""
Email Automation Tool - Demo Usage
This script demonstrates how to use the EmailAutomationTool class programmatically.
"""

from email_automation_tool import EmailAutomationTool

def demo_programmatic_usage():
    """Demonstrate programmatic usage of the Email Automation Tool."""
    print("🚀 Email Automation Tool - Programmatic Usage Demo")
    print("=" * 60)
    
    # Initialize the tool
    tool = EmailAutomationTool()
    
    # 1. Load recipients
    print("1. Loading recipients...")
    success = tool.load_recipients('sample_recipients.csv')
    if not success:
        print("❌ Failed to load recipients")
        return
    
    print(f"✅ Loaded {len(tool.recipients)} recipients")
    
    # 2. Configure email (you would need real credentials for this)
    print("\n2. Email configuration would go here...")
    print("   (In real usage, you would call tool.configure_email())")
    
    # 3. Compose email
    print("\n3. Composing email...")
    email_data = {
        'subject': 'Welcome to Our Newsletter!',
        'body': 'Dear {Name},\n\nWelcome to our newsletter! We\'re excited to have you join our community.\n\nBest regards,\nThe Newsletter Team',
        'format': 'plain',
        'attachments': []
    }
    print("✅ Email composed")
    
    # 4. Preview email
    print("\n4. Previewing email...")
    tool.preview_email(email_data)
    
    # 5. Show what bulk sending would look like
    print("\n5. Bulk email sending would happen here...")
    print("   (In real usage, you would call tool.send_bulk_emails(email_data))")
    
    print("\n✅ Demo completed!")
    print("\nTo send actual emails:")
    print("1. Run: python email_automation_tool.py")
    print("2. Configure your email settings")
    print("3. Use the interactive menu")

if __name__ == "__main__":
    demo_programmatic_usage()
