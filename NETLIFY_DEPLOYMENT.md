# 🚀 Netlify Deployment Guide for FastAPI Portfolio

## 📋 Pre-deployment Checklist

### 1. **Repository Setup**
- [ ] Push your code to GitHub/GitLab
- [ ] Ensure all files are committed
- [ ] Update any hardcoded URLs to use environment variables

### 2. **Environment Variables**
Set these in Netlify Dashboard > Site Settings > Environment Variables:
```
DEBUG=False
SECRET_KEY=your-super-secret-key-here
APP_NAME=FastAPI Portfolio
```

### 3. **Build Configuration**
The `netlify.toml` file is already configured with:
- Build command: `bash build.sh`
- Functions directory: `netlify/functions`
- Publish directory: `netlify/static`

## 🌐 Netlify Deployment Steps

### Step 1: Connect Repository
1. Log into [Netlify](https://app.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your Git provider (GitHub/GitLab)
4. Select your portfolio repository

### Step 2: Configure Build Settings
Netlify should auto-detect the settings from `netlify.toml`, but verify:
- **Build command**: `bash build.sh`
- **Publish directory**: `netlify/static`
- **Functions directory**: `netlify/functions`

### Step 3: Environment Variables
In Netlify Dashboard:
1. Go to Site Settings → Environment Variables
2. Add the required variables (see checklist above)
3. Generate a strong SECRET_KEY for production

### Step 4: Deploy
1. Click "Deploy site"
2. Wait for build to complete
3. Test all functionality

## 🔧 Local Testing

### Test the build process:
```bash
# Run the build script
bash build.sh

# Test locally with Python
cd netlify/functions
python -c "from app import handler; print('Handler loaded successfully!')"
```

### Test the full application:
```bash
# Start development server
python -m uvicorn app.main:app --reload
```

## 📁 File Structure for Deployment

```
netlify/
├── functions/
│   ├── app.py          # Netlify function handler
│   ├── app/            # FastAPI application
│   ├── data/           # JSON data files
│   ├── templates/      # Jinja2 templates
│   └── .env           # Environment variables
└── static/             # Static assets (CSS, JS, images)
```

## 🛠 Troubleshooting

### Build Failures
1. Check Python version compatibility (3.9+ required)
2. Verify all dependencies in `requirements.txt`
3. Check build logs in Netlify dashboard

### Function Errors
1. Ensure `mangum` is in requirements.txt
2. Check environment variables are set
3. Verify file paths in function handler

### Static Files Not Loading
1. Check static file paths in templates
2. Verify netlify.toml redirects
3. Ensure files are in `netlify/static/`

## 🎯 Post-Deployment

### 1. Test All Features
- [ ] Homepage loads correctly
- [ ] Admin login works
- [ ] CRUD operations function
- [ ] Contact form submits
- [ ] Dark/Light theme toggle

### 2. Performance Optimization
- [ ] Enable gzip compression in Netlify
- [ ] Set up CDN caching rules
- [ ] Monitor function execution times

### 3. Security
- [ ] Update SECRET_KEY in production
- [ ] Configure CORS properly
- [ ] Set up rate limiting if needed

## 📈 Monitoring

Check these in Netlify Dashboard:
- Function logs
- Build logs
- Analytics
- Performance metrics

## 🔄 Updates

To deploy updates:
1. Push changes to your repository
2. Netlify will auto-deploy from the main branch
3. Monitor build logs for any issues

---

**Your FastAPI Portfolio is now ready for Netlify deployment! 🎉**
