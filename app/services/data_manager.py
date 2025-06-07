from typing import List, Optional, Dict, Any
import uuid
from datetime import datetime
import logging

from app.services.json_utils import JSONFileHandler
from app.models.project import Project, ProjectCreate, ProjectUpdate
from app.models.skill import Skill, SkillCreate, SkillUpdate
from app.models.contact import ContactMessage, ContactMessageCreate, ContactMessageUpdate, AboutInfo, AboutInfoUpdate
from app.models.user import User, UserCreate
from app.models.education import Education, EducationCreate, EducationUpdate
from app.models.experience import Experience, ExperienceCreate, ExperienceUpdate
from app.models.certification import Certification, CertificationCreate, CertificationUpdate

logger = logging.getLogger(__name__)


class DataManager:
    """Centralized data manager for handling CRUD operations on JSON files."""
    
    def __init__(self, data_dir: str = "data"):
        self.json_handler = JSONFileHandler(data_dir)
        self._cache = {}
        self._cache_expiry = {}
        self.cache_duration = 300  # 5 minutes
    
    def _get_cache_key(self, filename: str) -> str:
        """Generate cache key for a file."""
        return f"cache_{filename}"
    
    def _is_cache_valid(self, filename: str) -> bool:
        """Check if cached data is still valid."""
        cache_key = self._get_cache_key(filename)
        if cache_key not in self._cache_expiry:
            return False
        
        return datetime.now().timestamp() < self._cache_expiry[cache_key]
    
    def _set_cache(self, filename: str, data: Dict[str, Any]) -> None:
        """Set cached data with expiry."""
        cache_key = self._get_cache_key(filename)
        self._cache[cache_key] = data
        self._cache_expiry[cache_key] = datetime.now().timestamp() + self.cache_duration
    
    def _get_cached_data(self, filename: str) -> Optional[Dict[str, Any]]:
        """Get cached data if valid."""
        if self._is_cache_valid(filename):
            cache_key = self._get_cache_key(filename)
            return self._cache.get(cache_key)
        return None
    
    def _clear_cache(self, filename: str) -> None:
        """Clear cache for a specific file."""
        cache_key = self._get_cache_key(filename)
        if cache_key in self._cache:
            del self._cache[cache_key]
        if cache_key in self._cache_expiry:
            del self._cache_expiry[cache_key]
    
    def _load_data(self, filename: str) -> Dict[str, Any]:
        """Load data from file with caching."""
        cached_data = self._get_cached_data(filename)
        if cached_data is not None:
            logger.debug(f"Using cached data for {filename}")
            return cached_data
        
        data = self.json_handler.read_json(filename)
        self._set_cache(filename, data)
        return data
    
    def _save_data(self, filename: str, data: Dict[str, Any]) -> None:
        """Save data to file and update cache."""
        self.json_handler.write_json(filename, data)
        self._set_cache(filename, data)
    
    # Project operations
    def get_all_projects(self) -> List[Project]:
        """Get all projects."""
        try:
            data = self._load_data("projects.json")
            projects_data = data.get("projects", [])
            return [Project(**project) for project in projects_data]
        except Exception as e:
            logger.error(f"Error getting projects: {e}")
            return []
    
    def get_project_by_id(self, project_id: str) -> Optional[Project]:
        """Get a project by ID."""
        projects = self.get_all_projects()
        for project in projects:
            if project.id == project_id:
                return project
        return None
    
    def create_project(self, project_data: ProjectCreate) -> Project:
        """Create a new project."""
        try:
            data = self._load_data("projects.json")
            projects = data.get("projects", [])
            
            # Generate unique ID
            project_id = str(uuid.uuid4())
            
            # Create project with ID and timestamp
            new_project = Project(
                id=project_id,
                **project_data.dict()
            )
            
            projects.append(new_project.dict())
            data["projects"] = projects
            
            self._save_data("projects.json", data)
            logger.info(f"Created project: {new_project.title}")
            return new_project
        except Exception as e:
            logger.error(f"Error creating project: {e}")
            raise
    
    def update_project(self, project_id: str, project_data: ProjectUpdate) -> Optional[Project]:
        """Update an existing project."""
        try:
            data = self._load_data("projects.json")
            projects = data.get("projects", [])
            
            for i, project in enumerate(projects):
                if project["id"] == project_id:
                    # Update only provided fields
                    update_dict = project_data.dict(exclude_unset=True)
                    projects[i].update(update_dict)
                    
                    data["projects"] = projects
                    self._save_data("projects.json", data)
                    
                    updated_project = Project(**projects[i])
                    logger.info(f"Updated project: {project_id}")
                    return updated_project
            
            return None
        except Exception as e:
            logger.error(f"Error updating project {project_id}: {e}")
            raise
    
    def delete_project(self, project_id: str) -> bool:
        """Delete a project."""
        try:
            data = self._load_data("projects.json")
            projects = data.get("projects", [])
            
            initial_count = len(projects)
            projects = [p for p in projects if p["id"] != project_id]
            
            if len(projects) < initial_count:
                data["projects"] = projects
                self._save_data("projects.json", data)
                logger.info(f"Deleted project: {project_id}")
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error deleting project {project_id}: {e}")
            return False
    
    # Skill operations
    def get_all_skills(self) -> List[Skill]:
        """Get all skills."""
        try:
            data = self._load_data("skills.json")
            skills_data = data.get("skills", [])
            return [Skill(**skill) for skill in skills_data]
        except Exception as e:
            logger.error(f"Error getting skills: {e}")
            return []
    
    def get_skill_by_id(self, skill_id: str) -> Optional[Skill]:
        """Get a skill by ID."""
        skills = self.get_all_skills()
        for skill in skills:
            if skill.id == skill_id:
                return skill
        return None
    
    def create_skill(self, skill_data: SkillCreate) -> Skill:
        """Create a new skill."""
        try:
            data = self._load_data("skills.json")
            skills = data.get("skills", [])
            
            # Generate unique ID
            skill_id = str(uuid.uuid4())
            
            # Create skill with ID
            new_skill = Skill(
                id=skill_id,
                **skill_data.dict()
            )
            
            skills.append(new_skill.dict())
            data["skills"] = skills
            
            self._save_data("skills.json", data)
            logger.info(f"Created skill: {new_skill.name}")
            return new_skill
        except Exception as e:
            logger.error(f"Error creating skill: {e}")
            raise
    
    def update_skill(self, skill_id: str, skill_data: SkillUpdate) -> Optional[Skill]:
        """Update an existing skill."""
        try:
            data = self._load_data("skills.json")
            skills = data.get("skills", [])
            
            for i, skill in enumerate(skills):
                if skill["id"] == skill_id:
                    # Update only provided fields
                    update_dict = skill_data.dict(exclude_unset=True)
                    skills[i].update(update_dict)
                    
                    data["skills"] = skills
                    self._save_data("skills.json", data)
                    
                    updated_skill = Skill(**skills[i])
                    logger.info(f"Updated skill: {skill_id}")
                    return updated_skill
            
            return None
        except Exception as e:
            logger.error(f"Error updating skill {skill_id}: {e}")
            raise
    
    def delete_skill(self, skill_id: str) -> bool:
        """Delete a skill."""
        try:
            data = self._load_data("skills.json")
            skills = data.get("skills", [])
            
            initial_count = len(skills)
            skills = [s for s in skills if s["id"] != skill_id]
            
            if len(skills) < initial_count:
                data["skills"] = skills
                self._save_data("skills.json", data)
                logger.info(f"Deleted skill: {skill_id}")
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error deleting skill {skill_id}: {e}")
            return False
    
    # Contact message operations
    def get_all_messages(self) -> List[ContactMessage]:
        """Get all contact messages."""
        try:
            data = self._load_data("messages.json")
            messages_data = data.get("messages", [])
            return [ContactMessage(**message) for message in messages_data]
        except Exception as e:
            logger.error(f"Error getting messages: {e}")
            return []
    
    def create_message(self, message_data: ContactMessageCreate) -> ContactMessage:
        """Create a new contact message."""
        try:
            data = self._load_data("messages.json")
            messages = data.get("messages", [])
            
            # Generate unique ID
            message_id = str(uuid.uuid4())
            
            # Create message with ID and timestamp
            new_message = ContactMessage(
                id=message_id,
                **message_data.dict()
            )
            
            messages.append(new_message.dict())
            data["messages"] = messages
            
            self._save_data("messages.json", data)
            logger.info(f"Created message from: {new_message.email}")
            return new_message
        except Exception as e:
            logger.error(f"Error creating message: {e}")
            raise
    
    def update_message(self, message_id: str, message_data: ContactMessageUpdate) -> Optional[ContactMessage]:
        """Update a contact message (e.g., mark as read)."""
        try:
            data = self._load_data("messages.json")
            messages = data.get("messages", [])
            
            for i, message in enumerate(messages):
                if message["id"] == message_id:
                    # Update only provided fields
                    update_dict = message_data.dict(exclude_unset=True)
                    messages[i].update(update_dict)
                    
                    data["messages"] = messages
                    self._save_data("messages.json", data)
                    
                    updated_message = ContactMessage(**messages[i])
                    logger.info(f"Updated message: {message_id}")
                    return updated_message
            
            return None
        except Exception as e:
            logger.error(f"Error updating message {message_id}: {e}")
            raise

    def delete_message(self, message_id: str) -> bool:
        """Delete a contact message."""
        try:
            data = self._load_data("messages.json")
            messages = data.get("messages", [])
            
            initial_count = len(messages)
            messages = [m for m in messages if m["id"] != message_id]
            
            if len(messages) < initial_count:
                data["messages"] = messages
                self._save_data("messages.json", data)
                logger.info(f"Deleted message: {message_id}")
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error deleting message {message_id}: {e}")
            return False
    
    # About info operations
    def get_about_info(self) -> Optional[AboutInfo]:
        """Get about information."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            return AboutInfo(**about_data) if about_data else None
        except Exception as e:
            logger.error(f"Error getting about info: {e}")
            return None
    
    def update_about_info(self, about_data: AboutInfoUpdate) -> Optional[AboutInfo]:
        """Update about information."""
        try:
            data = self._load_data("about.json")
            current_about = data.get("about", {})
            
            # Update only provided fields
            update_dict = about_data.dict(exclude_unset=True)
            current_about.update(update_dict)
            
            data["about"] = current_about
            self._save_data("about.json", data)
            
            updated_about = AboutInfo(**current_about)
            logger.info("Updated about info")
            return updated_about
        except Exception as e:
            logger.error(f"Error updating about info: {e}")
            raise
    
    # User operations
    def get_all_users(self) -> List[User]:
        """Get all users."""
        try:
            data = self._load_data("users.json")
            users_data = data.get("users", [])
            logger.info(f"Loaded {len(users_data)} users from users.json")
            
            # Debug user data structure
            for i, user_data in enumerate(users_data):
                logger.debug(f"User {i+1} data keys: {user_data.keys()}")
            
            users = []
            for user_data in users_data:
                try:
                    user = User(**user_data)
                    users.append(user)
                except Exception as e:
                    logger.error(f"Error creating user object: {e}")
            
            logger.info(f"Returning {len(users)} valid user objects")
            return users
        except Exception as e:
            logger.error(f"Error getting users: {e}")
            return []
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Get a user by username."""
        users = self.get_all_users()
        for user in users:
            if user.username == username:
                return user
        return None
    
    def create_user(self, user_data: UserCreate, hashed_password: str) -> User:
        """Create a new user."""
        try:
            data = self._load_data("users.json")
            users = data.get("users", [])
            
            # Create user with hashed password
            new_user = User(
                username=user_data.username,
                email=getattr(user_data, 'email', None),
                hashed_password=hashed_password
            )
            
            users.append(new_user.dict())
            data["users"] = users
            
            self._save_data("users.json", data)
            logger.info(f"Created user: {new_user.username}")
            return new_user
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise

    # Education operations
    def get_all_educations(self) -> List[Education]:
        """Get all education entries."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            education_data = about_data.get("education", [])
            return [Education(**edu) for edu in education_data if isinstance(edu, dict) and "id" in edu]
        except Exception as e:
            logger.error(f"Error getting education entries: {e}")
            return []

    def get_education_by_id(self, education_id: str) -> Optional[Education]:
        """Get an education entry by ID."""
        educations = self.get_all_educations()
        for education in educations:
            if education.id == education_id:
                return education
        return None

    def create_education(self, education_data: EducationCreate) -> Education:
        """Create a new education entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            educations = about_data.get("education", [])
            
            # Generate unique ID
            education_id = str(uuid.uuid4())
            
            # Create education with ID
            new_education = Education(
                id=education_id,
                **education_data.dict()
            )
            
            educations.append(new_education.dict())
            about_data["education"] = educations
            data["about"] = about_data
            
            self._save_data("about.json", data)
            logger.info(f"Created education: {new_education.degree}")
            return new_education
        except Exception as e:
            logger.error(f"Error creating education: {e}")
            raise

    def update_education(self, education_id: str, education_data: EducationUpdate) -> Optional[Education]:
        """Update an existing education entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            educations = about_data.get("education", [])
            
            for i, education in enumerate(educations):
                if isinstance(education, dict) and education.get("id") == education_id:
                    # Update only provided fields
                    update_dict = education_data.dict(exclude_unset=True)
                    educations[i].update(update_dict)
                    
                    about_data["education"] = educations
                    data["about"] = about_data
                    self._save_data("about.json", data)
                    
                    updated_education = Education(**educations[i])
                    logger.info(f"Updated education: {education_id}")
                    return updated_education
            
            return None
        except Exception as e:
            logger.error(f"Error updating education {education_id}: {e}")
            raise

    def delete_education(self, education_id: str) -> bool:
        """Delete an education entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            educations = about_data.get("education", [])
            
            initial_count = len(educations)
            educations = [e for e in educations if not (isinstance(e, dict) and e.get("id") == education_id)]
            
            if len(educations) < initial_count:
                about_data["education"] = educations
                data["about"] = about_data
                self._save_data("about.json", data)
                logger.info(f"Deleted education: {education_id}")
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error deleting education {education_id}: {e}")
            return False

    # Experience operations
    def get_all_experiences(self) -> List[Experience]:
        """Get all experience entries."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            experience_data = about_data.get("experience", [])
            return [Experience(**exp) for exp in experience_data if isinstance(exp, dict) and "id" in exp]
        except Exception as e:
            logger.error(f"Error getting experience entries: {e}")
            return []

    def get_experience_by_id(self, experience_id: str) -> Optional[Experience]:
        """Get an experience entry by ID."""
        experiences = self.get_all_experiences()
        for experience in experiences:
            if experience.id == experience_id:
                return experience
        return None

    def create_experience(self, experience_data: ExperienceCreate) -> Experience:
        """Create a new experience entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            experiences = about_data.get("experience", [])
            
            # Generate unique ID
            experience_id = str(uuid.uuid4())
            
            # Create experience with ID
            new_experience = Experience(
                id=experience_id,
                **experience_data.dict()
            )
            
            experiences.append(new_experience.dict())
            about_data["experience"] = experiences
            data["about"] = about_data
            
            self._save_data("about.json", data)
            logger.info(f"Created experience: {new_experience.job_title}")
            return new_experience
        except Exception as e:
            logger.error(f"Error creating experience: {e}")
            raise

    def update_experience(self, experience_id: str, experience_data: ExperienceUpdate) -> Optional[Experience]:
        """Update an existing experience entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            experiences = about_data.get("experience", [])
            
            for i, experience in enumerate(experiences):
                if isinstance(experience, dict) and experience.get("id") == experience_id:
                    # Update only provided fields
                    update_dict = experience_data.dict(exclude_unset=True)
                    experiences[i].update(update_dict)
                    
                    about_data["experience"] = experiences
                    data["about"] = about_data
                    self._save_data("about.json", data)
                    
                    updated_experience = Experience(**experiences[i])
                    logger.info(f"Updated experience: {experience_id}")
                    return updated_experience
            
            return None
        except Exception as e:
            logger.error(f"Error updating experience {experience_id}: {e}")
            raise

    def delete_experience(self, experience_id: str) -> bool:
        """Delete an experience entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            experiences = about_data.get("experience", [])
            
            initial_count = len(experiences)
            experiences = [e for e in experiences if not (isinstance(e, dict) and e.get("id") == experience_id)]
            
            if len(experiences) < initial_count:
                about_data["experience"] = experiences
                data["about"] = about_data
                self._save_data("about.json", data)
                logger.info(f"Deleted experience: {experience_id}")
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error deleting experience {experience_id}: {e}")
            return False

    # Certification operations
    def get_all_certifications(self) -> List[Certification]:
        """Get all certification entries."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            certification_data = about_data.get("certifications", [])
            return [Certification(**cert) for cert in certification_data if isinstance(cert, dict) and "id" in cert]
        except Exception as e:
            logger.error(f"Error getting certification entries: {e}")
            return []

    def get_certification_by_id(self, certification_id: str) -> Optional[Certification]:
        """Get a certification entry by ID."""
        certifications = self.get_all_certifications()
        for certification in certifications:
            if certification.id == certification_id:
                return certification
        return None

    def create_certification(self, certification_data: CertificationCreate) -> Certification:
        """Create a new certification entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            certifications = about_data.get("certifications", [])
            
            # Generate unique ID
            certification_id = str(uuid.uuid4())
            
            # Create certification with ID
            new_certification = Certification(
                id=certification_id,
                **certification_data.dict()
            )
            
            certifications.append(new_certification.dict())
            about_data["certifications"] = certifications
            data["about"] = about_data
            
            self._save_data("about.json", data)
            logger.info(f"Created certification: {new_certification.name}")
            return new_certification
        except Exception as e:
            logger.error(f"Error creating certification: {e}")
            raise

    def update_certification(self, certification_id: str, certification_data: CertificationUpdate) -> Optional[Certification]:
        """Update an existing certification entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            certifications = about_data.get("certifications", [])
            
            for i, certification in enumerate(certifications):
                if isinstance(certification, dict) and certification.get("id") == certification_id:
                    # Update only provided fields
                    update_dict = certification_data.dict(exclude_unset=True)
                    certifications[i].update(update_dict)
                    
                    about_data["certifications"] = certifications
                    data["about"] = about_data
                    self._save_data("about.json", data)
                    
                    updated_certification = Certification(**certifications[i])
                    logger.info(f"Updated certification: {certification_id}")
                    return updated_certification
            
            return None
        except Exception as e:
            logger.error(f"Error updating certification {certification_id}: {e}")
            raise

    def delete_certification(self, certification_id: str) -> bool:
        """Delete a certification entry."""
        try:
            data = self._load_data("about.json")
            about_data = data.get("about", {})
            certifications = about_data.get("certifications", [])
            
            initial_count = len(certifications)
            certifications = [c for c in certifications if not (isinstance(c, dict) and c.get("id") == certification_id)]
            
            if len(certifications) < initial_count:
                about_data["certifications"] = certifications
                data["about"] = about_data
                self._save_data("about.json", data)
                logger.info(f"Deleted certification: {certification_id}")
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error deleting certification {certification_id}: {e}")
            return False
