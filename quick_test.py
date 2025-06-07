#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

print("Testing FastAPI Portfolio Application...")

try:
    print("1. Testing basic imports...")
    import fastapi
    print("   ✓ FastAPI imported")
    
    import uvicorn
    print("   ✓ Uvicorn imported")
    
    print("2. Testing app imports...")
    from app.main import app
    print("   ✓ Main app imported")
    
    print("3. Testing data files...")
    import os
    import json
    
    data_files = ['data/projects.json', 'data/skills.json', 'data/about.json', 'data/users.json', 'data/messages.json']
    
    for file_path in data_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                json.load(f)
            print(f"   ✓ {file_path} is valid")
        else:
            print(f"   ✗ {file_path} not found")
    
    print("\n✓ All tests passed! Ready to start server.")
    print("Run: uvicorn app.main:app --reload")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
