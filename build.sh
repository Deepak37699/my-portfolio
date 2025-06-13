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

# Create simple JavaScript Netlify function files
echo "Creating JavaScript Netlify function files..."

# Create api.js function
cat > netlify/functions/api.js << 'EOF'
// Simple API handler for Netlify Functions
exports.handler = async function(event, context) {
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*"
    },
    body: JSON.stringify({
      message: "API function working!",
      status: "success",
      timestamp: new Date().toISOString()
    })
  };
};
EOF

# Create index.js function
cat > netlify/functions/index.js << 'EOF'
// Simple index handler for Netlify Functions
exports.handler = async function(event, context) {
  return {
    statusCode: 200,
    headers: {
      "Content-Type": "text/html"
    },
    body: `
      <!DOCTYPE html>
      <html>
        <head>
          <title>Netlify Functions Test</title>
          <style>
            body {
              font-family: Arial, sans-serif;
              max-width: 800px;
              margin: 0 auto;
              padding: 20px;
            }
            pre {
              background: #f4f4f4;
              padding: 10px;
              border-radius: 5px;
            }
          </style>
        </head>
        <body>
          <h1>Netlify Functions Test</h1>
          <p>This is a JavaScript function responding to your request.</p>
          
          <h2>Request Details:</h2>
          <pre>
Path: \${event.path}
Method: \${event.httpMethod}
          </pre>
          
          <p><a href="/api">Test the API endpoint</a></p>
        </body>
      </html>
    `
  };
};
EOF

# Create Netlify function files
echo "Creating Netlify function files..."

# Create api.py function (simple JSON endpoint)
cat > netlify/functions/api.py << 'EOF'
def handler(event, context):
    """
    Simple API test function for Netlify
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '{"message": "API function working!", "status": "success"}'
    }
EOF

# Create index.py function (main entry point)
cat > netlify/functions/index.py << 'EOF'
import json
import os

def handler(event, context):
    """
    Simple index function for Netlify
    """
    path = event.get('path', '/')
    http_method = event.get('httpMethod', 'GET')
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        },
        'body': f"""<!DOCTYPE html>
<html>
<head>
    <title>Portfolio App</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
    </style>
</head>
<body>
    <h1>Portfolio Application</h1>
    <p>This is a simple Netlify Function responding to your request.</p>
    
    <h2>Request Details:</h2>
    <pre>
Path: {path}
Method: {http_method}
    </pre>
    
    <h2>Environment:</h2>
    <pre>
Python Path: {os.environ.get('PYTHONPATH', 'Not set')}
Working Directory: {os.getcwd()}
    </pre>
    
    <p><a href="/api">Test the API endpoint</a></p>
</body>
</html>"""
    }
EOF

# Create main.py function
cat > netlify/functions/main.py << 'EOF'
"""
Netlify Functions entry point for FastAPI application
"""
import sys
import os
import json
from pathlib import Path

# Add the current directory to Python path for local imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def handler(event, context):
    """
    Netlify Functions entry point (note: function name must be 'handler')
    """
    debug_info = {
        'method': event.get('httpMethod', 'Unknown'),
        'path': event.get('path', '/'),
        'working_directory': os.getcwd(),
        'python_path': sys.path[:3]
    }
    
    try:
        # Import FastAPI app and Mangum
        from app.main import app
        from mangum import Mangum
        
        # Create the Netlify-compatible handler with proper settings
        mangum_handler = Mangum(
            app, 
            lifespan="off",
            text_mime_types=[
                "application/json",
                "application/javascript", 
                "application/xml",
                "application/vnd.api+json",
            ],
        )
        
        return mangum_handler(event, context)
        
    except ImportError as e:
        import traceback
        error_msg = f"Import error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html'},
            'body': f'''<!DOCTYPE html>
<html>
<head><title>Import Error</title></head>
<body>
<h1>Import Error</h1>
<pre>{error_msg}</pre>
<p>Current directory: {os.getcwd()}</p>
<p>Python path: {sys.path[:5]}</p>
<p>Debug info: {json.dumps(debug_info, indent=2)}</p>
</body>
</html>'''
        }
    except Exception as e:
        import traceback
        error_msg = f"General error: {e}\nTraceback: {traceback.format_exc()}"
        print(error_msg)
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html'},
            'body': f'''<!DOCTYPE html>
<html>
<head><title>Server Error</title></head>
<body>
<h1>Server Error</h1>
<pre>{error_msg}</pre>
<p>Debug info: {json.dumps(debug_info, indent=2)}</p>
</body>
</html>'''
        }
EOF

# Create test.py function
cat > netlify/functions/test.py << 'EOF'
def handler(event, context):
    """
    Simple test function to verify Netlify Functions are working
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        },
        'body': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Netlify Function Test</title>
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
        .success {
            color: #4ade80;
            font-size: 2rem;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="success">✅</div>
        <h1>Netlify Function Working!</h1>
        <p>This simple test function is running correctly.</p>
        <p><strong>Event:</strong> ''' + str(event.get('httpMethod', 'Unknown')) + ''' ''' + str(event.get('path', '/')) + '''</p>
        <p><strong>Next:</strong> <a href="/.netlify/functions/main" style="color: white;">Try FastAPI Function</a></p>
    </div>
</body>
</html>'''
    }
EOF

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
