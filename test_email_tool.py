#!/usr/bin/env python3
"""
Test script for Email Automation Tool
This script demonstrates basic functionality without sending actual emails.
"""

import os
import sys
from email_automation_tool import EmailAutomationTool

def test_recipient_loading():
    """Test recipient loading functionality."""
    print("🧪 Testing recipient loading...")
    
    tool = EmailAutomationTool()
    
    # Test CSV loading
    print("Testing CSV loading...")
    success = tool.load_recipients('sample_recipients.csv')
    if success:
        print(f"✅ CSV loaded successfully: {len(tool.recipients)} recipients")
    else:
        print("❌ CSV loading failed")
    
    # Test JSON loading
    print("Testing JSON loading...")
    success = tool.load_recipients('sample_recipients.json')
    if success:
        print(f"✅ JSON loaded successfully: {len(tool.recipients)} recipients")
    else:
        print("❌ JSON loading failed")

def test_email_composition():
    """Test email composition functionality."""
    print("\n🧪 Testing email composition...")
    
    tool = EmailAutomationTool()
    
    # Load sample recipients
    tool.load_recipients('sample_recipients.csv')
    
    # Test personalization
    test_message = "Hello {Name}! Your email is {Email}."
    test_recipient = {"name": "John Doe", "email": "john@example.com"}
    
    personalized = tool.personalize_message(test_message, test_recipient)
    expected = "Hello John Doe! Your email is john@example.com."
    
    if personalized == expected:
        print("✅ Personalization working correctly")
    else:
        print("❌ Personalization failed")
        print(f"Expected: {expected}")
        print(f"Got: {personalized}")

def test_file_validation():
    """Test file validation."""
    print("\n🧪 Testing file validation...")
    
    tool = EmailAutomationTool()
    
    # Test non-existent file
    success = tool.load_recipients('non_existent_file.csv')
    if not success:
        print("✅ Correctly handled non-existent file")
    else:
        print("❌ Should have failed for non-existent file")
    
    # Test invalid file format
    success = tool.load_recipients('README.md')
    if not success:
        print("✅ Correctly handled invalid file format")
    else:
        print("❌ Should have failed for invalid file format")

def main():
    """Run all tests."""
    print("🚀 Running Email Automation Tool Tests")
    print("=" * 50)
    
    try:
        test_recipient_loading()
        test_email_composition()
        test_file_validation()
        
        print("\n✅ All tests completed!")
        print("\nNote: This test script only validates functionality without sending actual emails.")
        print("To test email sending, run the main application and configure your email settings.")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
