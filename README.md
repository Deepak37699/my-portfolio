# FastAPI Portfolio Web Application

A modern, responsive portfolio website built with FastAPI, featuring an admin panel for content management and JWT-based authentication.

## 🚀 Features

- **Responsive Portfolio Website**: Modern, animated design that works on all devices
- **Admin Panel**: Full CRUD operations for projects, skills, and content management
- **Authentication System**: JWT-based authentication with secure login/logout
- **Contact Form**: Message storage and management system
- **JSON Storage**: File-based data storage (no database required)
- **Modern UI**: Beautiful animations and transitions
- **SEO Friendly**: Server-side rendering with Jinja2 templates

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)

## 🛠️ Installation & Setup

### 1. Clone or Download the Project
```bash
# Navigate to the project directory
cd "d:\Deepak Yadav\Portfolio\my-portfolio"
```

### 2. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Run Setup (First Time Only)
```bash
# Run the setup script to create admin user and data files
python setup.py
```

### 4. Start the Server
```bash
# Start the FastAPI development server
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Or simply double-click `start_server.bat`**

### 5. Access the Application
- **Website**: http://127.0.0.1:8000
- **Admin Login**: http://127.0.0.1:8000/auth/login
- **API Documentation**: http://127.0.0.1:8000/docs

## 🔐 Default Admin Credentials

- **Username**: `admin`
- **Password**: `admin123`

> ⚠️ **Important**: Change these credentials in production!

## 📁 Project Structure

```
my-portfolio/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── models/              # Pydantic data models
│   ├── routes/              # API route handlers
│   ├── services/            # Business logic and data management
│   └── utils/               # Utility functions (security, etc.)
├── data/                    # JSON data files
├── static/                  # CSS, JS, and image files
├── templates/               # Jinja2 HTML templates
├── .env                     # Environment configuration
├── requirements.txt         # Python dependencies
├── setup.py                 # Setup utility
└── start_server.bat         # Quick start script
```

## 🎨 Customization

### Adding Your Content

1. **Login to Admin Panel**: Visit `/auth/login` and use admin credentials
2. **Manage Projects**: Add your projects with descriptions, technologies, and links
3. **Update Skills**: Add your technical skills with proficiency levels
4. **Edit About Info**: Update your personal information and bio
5. **View Messages**: Check contact form submissions

### Customizing Appearance

- **CSS**: Edit `static/css/style.css` for styling changes
- **Templates**: Modify HTML templates in the `templates/` directory
- **Images**: Add your photos to `static/images/`

### Configuration

Edit the `.env` file to configure:
- JWT secret key
- Admin credentials
- CORS settings
- File upload limits

## 🔧 API Endpoints

### Public Routes
- `GET /` - Home page
- `GET /about` - About page
- `GET /projects` - Projects page
- `GET /skills` - Skills page
- `GET /contact` - Contact page
- `POST /contact` - Submit contact form

### Admin Routes (Requires Authentication)
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/projects` - Manage projects
- `GET /admin/skills` - Manage skills
- `GET /admin/messages` - View messages
- `GET /admin/about` - Edit about info

### API Routes
- `GET /api/projects` - Get all projects
- `GET /api/skills` - Get all skills
- `POST /api/contact` - Submit contact message

## 📊 Data Management

The application uses JSON files for data storage:

- `data/projects.json` - Project information
- `data/skills.json` - Skills and proficiencies
- `data/about.json` - Personal information
- `data/users.json` - User accounts
- `data/messages.json` - Contact form messages

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt password hashing
- **CORS Protection**: Configurable CORS settings
- **Input Validation**: Pydantic model validation
- **XSS Protection**: Template auto-escaping

## 🚀 Deployment

### For Production:

1. **Update Configuration**:
   - Change `SECRET_KEY` in `.env`
   - Update admin credentials
   - Set `DEBUG=False`

2. **Use Production Server**:
   ```bash
   pip install gunicorn
   gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

3. **Serve Static Files**: Configure your web server (nginx/Apache) to serve static files

### Environment Variables

Create a `.env` file with:
```env
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEFAULT_ADMIN_USERNAME=admin
DEFAULT_ADMIN_PASSWORD=admin123
```

## 🐛 Troubleshooting

### Server Won't Start
- Check Python version: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Run setup: `python setup.py`

### Admin Login Issues
- Run setup script to create admin user
- Check `data/users.json` file exists
- Verify credentials in `.env` file

### Static Files Not Loading
- Check `static/` directory exists
- Verify file permissions
- Restart the server

## 📝 Development

### Adding New Features

1. **Models**: Add Pydantic models in `app/models/`
2. **Routes**: Create route handlers in `app/routes/`
3. **Templates**: Add HTML templates in `templates/`
4. **Services**: Add business logic in `app/services/`

### Testing

```bash
# Run tests (if implemented)
pytest

# Test specific components
python -c "from app.main import app; print('App loads successfully')"
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review the console/terminal output for error messages
3. Ensure all dependencies are installed
4. Verify the setup script completed successfully

---

**Enjoy building your portfolio! 🎉**
