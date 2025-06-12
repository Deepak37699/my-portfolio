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

# Copy root files needed for the application
echo "Copying additional files..."
cp requirements.txt netlify/functions/

# Copy environment file if it exists
if [ -f ".env.production" ]; then
    echo "Setting up production environment..."
    cp .env.production netlify/functions/.env
fi

# Create a simple index.html for the static directory
echo "Creating static index.html..."
cat > netlify/static/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI Portfolio</title>
    <meta http-equiv="refresh" content="0; url=/.netlify/functions/main/">
</head>
<body>
    <p>Redirecting to portfolio...</p>
</body>
</html>
EOF

echo "Build process completed successfully!"
