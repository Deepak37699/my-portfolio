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

# Copy environment file if it exists
if [ -f ".env.production" ]; then
    echo "Setting up production environment..."
    cp .env.production netlify/functions/.env
fi

echo "Build process completed successfully!"
