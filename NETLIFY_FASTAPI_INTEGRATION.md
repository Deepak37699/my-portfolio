# Netlify FastAPI Integration Guide

## Overview

This document provides guidance on integrating your FastAPI application with Netlify Functions. We initially encountered 404 errors when trying to deploy Python-based functions directly. The solution was to use JavaScript functions as an entry point, which can then interface with your Python backend if needed.

## Current Architecture

1. **JavaScript Functions (Working)**
   - `api.js` - Simple JSON API endpoint
   - `index.js` - HTML response for root and other paths
   - `main.js` - Portfolio application with multiple routes

2. **Configuration**
   - `netlify.toml` - Defines build settings and redirects
   - `build.sh` - Handles the build process for Netlify

## Future Integration Options

### Option 1: JavaScript-First Approach

Continue using JavaScript functions as the primary entry point and gradually integrate your FastAPI app:

1. Create JavaScript handlers for all routes.
2. Use fetch/axios to call your Python API endpoints when deployed elsewhere.
3. Maintain separate deployments for frontend (Netlify) and backend (e.g., Heroku, AWS).

### Option 2: Advanced JavaScript-Python Integration

Use JavaScript functions as wrappers that call Python scripts:

1. Use Node.js `child_process` to execute Python scripts.
2. Install Python dependencies during build.
3. Pass request data to Python and return the response.

Example:
```javascript
const { spawn } = require('child_process');

exports.handler = async function(event, context) {
  return new Promise((resolve, reject) => {
    // Execute Python script
    const pythonProcess = spawn('python', ['path/to/script.py', JSON.stringify(event)]);
    
    let output = '';
    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        return reject(`Python process exited with code ${code}`);
      }
      resolve({
        statusCode: 200,
        body: output
      });
    });
  });
};
```

### Option 3: Static Site + API

Convert your FastAPI app to a static site with JavaScript API calls:

1. Use FastAPI to generate static HTML/CSS/JS files.
2. Deploy these static files to Netlify.
3. Create JavaScript functions for dynamic content.
4. Deploy your FastAPI backend separately and have the static site call it via API.

## Next Steps

1. **Choose an Integration Approach**: Decide which option best fits your needs.
2. **Develop Integration Plan**: Create detailed implementation steps.
3. **Update Build Scripts**: Modify build scripts to support the chosen approach.
4. **Testing**: Implement thorough testing of the integrated solution.
5. **Documentation**: Update documentation for future reference.

## Resources

- [Netlify Functions Documentation](https://docs.netlify.com/functions/overview/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [JavaScript-Python Integration Examples](https://github.com/netlify-labs/netlify-python-utils)
