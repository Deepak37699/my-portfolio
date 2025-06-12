#!/usr/bin/env python3
"""
Test script to verify the Netlify function works correctly
"""
import sys
import os
from pathlib import Path

# Add netlify functions directory to path
functions_dir = Path(__file__).parent / "netlify" / "functions"
sys.path.insert(0, str(functions_dir))

def test_function():
    """Test the Netlify function locally"""
    try:
        # Import the handler
        from main import handler
        
        # Create a mock event and context (similar to what Netlify sends)
        mock_event = {
            "httpMethod": "GET",
            "path": "/",
            "headers": {
                "host": "localhost:8000",
                "user-agent": "test-agent"
            },
            "queryStringParameters": None,
            "body": None,
            "isBase64Encoded": False
        }
        
        mock_context = {
            "requestId": "test-request-id",
            "stage": "test"
        }
        
        # Call the handler
        response = handler(mock_event, mock_context)
        
        print("✅ Function test successful!")
        print(f"Status Code: {response.get('statusCode', 'Unknown')}")
        print(f"Headers: {response.get('headers', {})}")
        
        # Check if it's an HTML response
        body = response.get('body', '')
        if 'html' in body.lower():
            print("📄 Response contains HTML content")
        
        return True
        
    except Exception as e:
        print(f"❌ Function test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing Netlify function...")
    success = test_function()
    sys.exit(0 if success else 1)
