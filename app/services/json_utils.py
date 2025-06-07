import json
import os
import time
import threading
from typing import Any, Dict, List, Optional
from pathlib import Path
import logging

# Cross-platform file locking using threading
_file_locks = {}
_lock_lock = threading.Lock()

logger = logging.getLogger(__name__)


class JSONFileHandler:
    """Utility class for handling JSON file operations with locking mechanism."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
    
    def _get_file_lock(self, filename: str) -> threading.Lock:
        """Get or create a lock for a specific file."""
        with _lock_lock:
            if filename not in _file_locks:
                _file_locks[filename] = threading.Lock()
            return _file_locks[filename]
    
    def read_json(self, filename: str) -> Dict[str, Any]:
        """
        Read JSON data from file with error handling.
        
        Args:
            filename: Name of the JSON file
            
        Returns:
            Dictionary containing the JSON data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file contains invalid JSON
        """
        file_path = self.data_dir / filename
        
        if not file_path.exists():
            logger.warning(f"File {filename} not found, returning empty dict")
            return {}
        
        file_lock = self._get_file_lock(filename)
        
        try:
            with file_lock:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    logger.info(f"Successfully read {filename}")
                    return data
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {filename}: {e}")
            raise
        except Exception as e:
            logger.error(f"Error reading {filename}: {e}")
            raise
    
    def write_json(self, filename: str, data: Dict[str, Any]) -> None:
        """
        Write JSON data to file with locking mechanism.
        
        Args:
            filename: Name of the JSON file
            data: Dictionary to write as JSON
            
        Raises:
            ValueError: If data cannot be serialized to JSON
        """
        file_path = self.data_dir / filename
        file_lock = self._get_file_lock(filename)
        
        try:
            with file_lock:
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=2, ensure_ascii=False, default=str)
                    logger.info(f"Successfully wrote {filename}")
        except (TypeError, ValueError) as e:
            logger.error(f"Cannot serialize data to JSON for {filename}: {e}")
            raise
        except Exception as e:
            logger.error(f"Error writing {filename}: {e}")
            raise
    
    def backup_file(self, filename: str) -> Optional[str]:
        """
        Create a backup of the JSON file.
        
        Args:
            filename: Name of the JSON file to backup
            
        Returns:
            Path to backup file if successful, None otherwise
        """
        try:
            source_path = self.data_dir / filename
            if not source_path.exists():
                logger.warning(f"Cannot backup {filename} - file does not exist")
                return None
            
            backup_filename = f"{filename}.backup"
            backup_path = self.data_dir / backup_filename
            
            data = self.read_json(filename)
            self.write_json(backup_filename, data)
            
            logger.info(f"Created backup: {backup_filename}")
            return str(backup_path)
        except Exception as e:
            logger.error(f"Error creating backup for {filename}: {e}")
            return None
    
    def file_exists(self, filename: str) -> bool:
        """Check if a JSON file exists."""
        return (self.data_dir / filename).exists()
    
    def get_file_size(self, filename: str) -> int:
        """Get the size of a JSON file in bytes."""
        file_path = self.data_dir / filename
        return file_path.stat().st_size if file_path.exists() else 0


def create_default_files():
    """Create default JSON files with initial data if they don't exist."""
    handler = JSONFileHandler()
    
    # Default projects data
    if not handler.file_exists("projects.json"):
        projects_data = {
            "projects": [
                {
                    "id": "project-1",
                    "title": "Portfolio Website",
                    "description": "Personal portfolio built with FastAPI and Jinja2 templates, featuring JSON-based storage and admin interface.",
                    "technologies": ["Python", "FastAPI", "Jinja2", "HTML/CSS", "JavaScript"],
                    "image": "portfolio.jpg",
                    "github_url": "https://github.com/username/portfolio",
                    "live_url": "https://myportfolio.com",
                    "featured": True,
                    "created_date": "2024-01-15T10:00:00"
                }
            ]
        }
        handler.write_json("projects.json", projects_data)
    
    # Default skills data
    if not handler.file_exists("skills.json"):
        skills_data = {
            "skills": [
                {
                    "id": "skill-1",
                    "name": "Python",
                    "category": "Programming Language",
                    "proficiency": 90,
                    "years_experience": 3,
                    "icon": "python-icon.svg"
                },
                {
                    "id": "skill-2",
                    "name": "FastAPI",
                    "category": "Web Framework",
                    "proficiency": 85,
                    "years_experience": 2,
                    "icon": "fastapi-icon.svg"
                },
                {
                    "id": "skill-3",
                    "name": "JavaScript",
                    "category": "Programming Language",
                    "proficiency": 80,
                    "years_experience": 4,
                    "icon": "js-icon.svg"
                }
            ]
        }
        handler.write_json("skills.json", skills_data)
    
    # Default about data
    if not handler.file_exists("about.json"):
        about_data = {
            "about": {
                "name": "Deepak Yadav",
                "title": "Full Stack Developer",
                "bio": "Passionate full-stack developer with expertise in Python, FastAPI, and modern web technologies. I love creating efficient, scalable solutions and learning new technologies.",
                "location": "India",
                "email": "deepak@example.com",
                "phone": "+91-9876543210",
                "linkedin": "https://linkedin.com/in/deepakyadav",
                "github": "https://github.com/deepakyadav",
                "resume_url": "https://example.com/resume.pdf",
                "profile_image": "profile.jpg"
            }
        }
        handler.write_json("about.json", about_data)
    
    # Default users data
    if not handler.file_exists("users.json"):
        users_data = {
            "users": []
        }
        handler.write_json("users.json", users_data)
    
    # Default messages data
    if not handler.file_exists("messages.json"):
        messages_data = {
            "messages": []
        }
        handler.write_json("messages.json", messages_data)
    
    logger.info("Default JSON files created successfully")
