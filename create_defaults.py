#!/usr/bin/env python3
import sys
sys.path.append('.')

from app.services.json_utils import create_default_files

if __name__ == "__main__":
    create_default_files()
    print("Default files created successfully!")
