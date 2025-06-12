#!/bin/bash
set -e

# Build script for Netlify deployment
echo "Starting build process..."

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating directories..."
mkdir -p netlify/static
mkdir -p netlify/functions

# Copy static files
echo "Copying static files..."
if [ -d "static" ]; then
    cp -r static/* netlify/static/ 2>/dev/null || true
fi

# Copy application files to functions directory
echo "Copying application files..."
cp -r app netlify/functions/
cp -r data netlify/functions/
cp -r templates netlify/functions/
cp -r static netlify/functions/

# Copy root files needed for the application
echo "Copying additional files..."
cp requirements.txt netlify/functions/

# Copy environment file if it exists
if [ -f ".env.production" ]; then
    echo "Setting up production environment..."
    cp .env.production netlify/functions/.env
fi

# Ensure the function has all dependencies
echo "Copying function requirements..."
if [ -f "netlify/functions/requirements.txt" ]; then
    # Merge requirements if they exist in functions directory
    cat requirements.txt >> netlify/functions/requirements.txt
    sort netlify/functions/requirements.txt | uniq > netlify/functions/requirements_temp.txt
    mv netlify/functions/requirements_temp.txt netlify/functions/requirements.txt
else
    cp requirements.txt netlify/functions/requirements.txt
fi

# Create a simple index.html for the static directory
echo "Creating static index.html..."
cat > netlify/static/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deepak Yadav - Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            text-align: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        .spinner {
            border: 4px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top: 4px solid white;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 1rem;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
    <script>
        // Redirect to the function after a short delay
        setTimeout(() => {
            window.location.href = '/.netlify/functions/main';
        }, 2000);
    </script>
</head>
<body>
    <div class="container">
        <div class="spinner"></div>
        <h1>Deepak Yadav</h1>
        <p>Loading portfolio...</p>
        <p><small>If you're not redirected automatically, <a href="/.netlify/functions/main" style="color: white;">click here</a>.</small></p>
    </div>
</body>
</html>
EOF

echo "Build process completed successfully!"
