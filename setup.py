#!/usr/bin/env python3
"""
Setup utility to create the default admin user for the FastAPI Portfolio application
"""
import os
import sys
import json
from datetime import datetime

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_admin_user():
    """Create the default admin user"""
    print("Setting up default admin user...")
    
    try:
        from app.utils.security import get_password_hash
        from app.models.user import User
        import uuid
        
        # Create admin user
        admin_user = User(
            id=str(uuid.uuid4()),
            username="admin",
            email="admin@portfolio.local",
            full_name="Administrator",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
            is_admin=True,
            created_date=datetime.now()
        )
          # Read existing users
        users_file = "data/users.json"
        if os.path.exists(users_file):
            with open(users_file, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    users_data = data.get("users", [])
                except Exception:
                    users_data = []
        else:
            users_data = []
        
        # Check if admin user already exists
        admin_exists = any(user.get('username') == 'admin' for user in users_data if isinstance(user, dict))
        
        if not admin_exists:            # Add admin user
            users_data.append(admin_user.dict())
            
            # Write back to file
            with open(users_file, 'w', encoding='utf-8') as f:
                json.dump({"users": users_data}, f, indent=2, default=str)
            
            print("✅ Admin user created successfully!")
            print("   Username: admin")
            print("   Password: admin123")
            print("   ⚠️  Change this password in production!")
        else:
            print("ℹ️  Admin user already exists.")
            
        return True
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")
        import traceback
        traceback.print_exc()
        return False

def ensure_data_directories():
    """Ensure all required directories exist"""
    print("Checking data directories...")
    
    directories = ['data', 'static/images', 'static/css', 'static/js']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"✅ Created directory: {directory}")
        else:
            print(f"✅ Directory exists: {directory}")

def check_data_files():
    """Check if all required data files exist"""
    print("Checking data files...")
    
    required_files = {
        'data/projects.json': [],
        'data/skills.json': [],
        'data/about.json': {
            "name": "Your Name",
            "title": "Full Stack Developer",
            "bio": "Welcome to my portfolio! I'm a passionate developer...",
            "location": "Your City, Country",
            "email": "your.email@example.com",
            "phone": "+1-234-567-8900",
            "linkedin": "https://linkedin.com/in/yourprofile",
            "github": "https://github.com/yourusername",
            "resume_url": "/static/resume.pdf",
            "profile_image": "/static/images/profile.jpg"
        },
        'data/users.json': [],
        'data/messages.json': []
    }
    
    for file_path, default_content in required_files.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(default_content, f, indent=2)
            print(f"✅ Created: {file_path}")
        else:
            print(f"✅ Exists: {file_path}")

def main():
    """Main setup function"""
    print("FastAPI Portfolio - Setup Utility")
    print("=" * 40)
    
    # Ensure directories exist
    ensure_data_directories()
    print()
    
    # Check/create data files
    check_data_files()
    print()
    
    # Create admin user
    admin_created = create_admin_user()
    print()
    
    if admin_created:
        print("🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Start the server: python -m uvicorn app.main:app --reload")
        print("2. Open http://127.0.0.1:8000 in your browser")
        print("3. Login with admin/admin123 to access admin panel")
        print("4. Customize your portfolio content through the admin interface")
    else:
        print("⚠️  Setup completed with warnings. Check the errors above.")

if __name__ == "__main__":
    main()
