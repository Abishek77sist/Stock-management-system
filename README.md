# README Folder Structure & Documentation Guide

## Recommended Folder Structure

```
project-root/
├── docs/
│   ├── README.md                    # Main project documentation
│   ├── FEATURES.md                  # Detailed features documentation
│   ├── TESTING.md                   # Testing documentation
│   ├── DEPLOYMENT.md                # Deployment guide
│   ├── API.md                       # API documentation (if applicable)
│   ├── CONTRIBUTING.md              # Contribution guidelines
│   ├── CHANGELOG.md                 # Version history
│   └── assets/                      # Documentation assets
│       ├── images/
│       │   ├── screenshots/
│       │   ├── diagrams/
│       │   └── logos/
│       ├── wireframes/
│       └── videos/
├── readme-assets/                   # Alternative: Keep at root level
│   ├── features/
│   ├── structure/
│   ├── validation/
│   └── skeleton/
└── README.md                        # Quick start guide (links to docs/)
```

## Implementation Steps

### Step 1: Create the Folder Structure

Create a `docs/` folder in your project root with the following structure:

```bash
mkdir -p docs/assets/{images/{screenshots,diagrams,logos},wireframes,videos}
```

### Step 2: Organize Existing Documentation

Move your existing documentation files:

```bash
# Move main documentation files
mv FEATURES.md docs/
mv TESTING.md docs/

# Move readme assets
mv readme-assets/ docs/assets/images/
```

### Step 3: Create Main README.md

Your root `README.md` should be a concise overview with links to detailed documentation:

```markdown
# Stock Management System

A full-stack inventory management application built with Python Flask and MongoDB.

![Application Screenshot](docs/assets/images/screenshots/dashboard.png)

## 🚀 Quick Start

[Installation Guide](docs/README.md#installation) | [Features](docs/FEATURES.md) | [API Docs](docs/API.md)

## 📋 Overview

StockMGMT helps small business owners automate stock tracking and eliminate manual spreadsheet management.

### Key Features
- Multi-user access with role-based permissions
- Real-time inventory tracking
- Supplier and category management
- Pending stock order workflow
- Low stock alerts

## 🛠️ Tech Stack

- **Backend**: Python Flask, MongoEngine
- **Database**: MongoDB
- **Frontend**: Bootstrap 5, jQuery, JavaScript
- **Authentication**: Flask-User
- **Forms**: Flask-WTF, WTForms

## 📖 Documentation

- [Complete Documentation](docs/README.md)
- [Features Guide](docs/FEATURES.md)
- [Testing Documentation](docs/TESTING.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [API Reference](docs/API.md)

## 🎯 Quick Links

- [Live Demo](http://ms3-stockmgmt.herokuapp.com/)
- [Report Issues](https://github.com/yourusername/project/issues)
- [Contribute](docs/CONTRIBUTING.md)

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

## 👥 Maintainer

**Vamshi S**  
📧 [vamshis954@gmail.com](mailto:vamshis954@gmail.com)  
🔗 [GitHub](https://github.com/Vamshi5S/Stock_Management_main.git)
```

### Step 4: Create Comprehensive docs/README.md

This is your main detailed documentation file:

```markdown
# Stock Management System - Complete Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [User Experience (UX)](#user-experience)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)

## Introduction

### Project Overview
This Stock Management application is a full-stack solution designed for small businesses...

### Problem Statement
Many small businesses struggle with manual inventory tracking...

### Solution
StockMGMT provides an automated, web-based solution...

## User Experience

### User Stories
- [View User Stories](FEATURES.md#user-stories)

### Design Philosophy
- Mobile-first responsive design
- Intuitive navigation
- Clean, professional interface

### Color Scheme
- Primary: Blue (#007bff) - Trust and professionalism
- Success: Green (#28a745) - Completed actions
- Warning: Yellow (#ffc107) - Pending items
- Danger: Red (#dc3545) - Delete actions

## Architecture

### System Design
[View Architecture Diagram](assets/images/diagrams/architecture.png)

### Database Schema
[View Database Design](assets/images/diagrams/database-schema.png)

### Technology Stack
- **Framework**: Flask 2.0.2
- **Database**: MongoDB with MongoEngine
- **Authentication**: Flask-User
- **Frontend**: Bootstrap 5.1
- **JavaScript**: jQuery 3.5.1

## Installation

### Prerequisites
- Python 3.8+
- MongoDB 4.0+
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/Vamshi5S/Stock_Management_main.git
cd Stock_Management_main
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp env.py.example env.py
# Edit env.py with your configuration
```

5. **Run the application**
```bash
python app.py
```

Visit `http://localhost:5000`

## Configuration

### Environment Variables

Create an `env.py` file in the root directory:

```python
import os

os.environ.setdefault('IP', '0.0.0.0')
os.environ.setdefault('PORT', '5000')
os.environ.setdefault('SECRET_KEY', 'your-secret-key')
os.environ.setdefault('MONGO_URI', 'mongodb://localhost:27017/stockmgmt')
os.environ.setdefault('MONGO_DBNAME', 'stockmgmt')

# Email Configuration (for Flask-User)
os.environ.setdefault('MAIL_SERVER', 'smtp.gmail.com')
os.environ.setdefault('MAIL_PORT', '587')
os.environ.setdefault('MAIL_USERNAME', 'your-email@gmail.com')
os.environ.setdefault('MAIL_PASSWORD', 'your-app-password')
os.environ.setdefault('USER_EMAIL_SENDER_EMAIL', 'your-email@gmail.com')

os.environ.setdefault('DEBUG', 'True')
```

### MongoDB Setup

1. Create a MongoDB Atlas cluster or use local MongoDB
2. Create a database named `stockmgmt`
3. Update the `MONGO_URI` in `env.py`

## Usage

### For Business Owners (Admin)
- [Complete Admin Guide](FEATURES.md#admin-features)

### For Staff Users
- [Staff User Guide](FEATURES.md#staff-features)

### Common Workflows

#### Adding New Products
1. Navigate to Categories → Create categories
2. Navigate to Suppliers → Add supplier information
3. Navigate to Products → Create new product
4. Assign category and supplier

#### Managing Stock
1. Dashboard shows low stock alerts
2. Update stock directly from product page
3. Create pending stock orders for deliveries
4. Approve pending orders when stock arrives

## Testing

See [TESTING.md](TESTING.md) for comprehensive testing documentation.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment instructions to:
- Heroku
- AWS
- Google Cloud Platform
- Other platforms

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Credits

### Code References
- Flask documentation
- MongoEngine documentation
- Bootstrap 5 documentation
- Flask-User package

### Assets
- Icons: Bootstrap Icons
- Fonts: Google Fonts (Roboto)
- Images: Pexels


## Contact

**Abishek  P**  
Email: [abishek050205@gmail.com](mailto:abishek050205@gmail.com)  
GitHub: [Abisheksist77](https://github.com/Abishek77sist/Stock-management-system)
```

## Additional Documentation Files

### docs/DEPLOYMENT.md

```markdown
# Deployment Guide

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git repository

### Steps

1. **Prepare Application**
```bash
# Ensure requirements.txt is updated
pip freeze > requirements.txt

# Create Procfile
echo "web: python app.py" > Procfile
```

2. **Create Heroku App**
```bash
heroku login
heroku create your-app-name
```

3. **Configure Environment Variables**
```bash
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set MONGO_URI="your-mongodb-uri"
# ... set all other variables
```

4. **Deploy**
```bash
git push heroku main
```

## AWS Deployment
[Add AWS deployment instructions]

## Docker Deployment
[Add Docker deployment instructions]
```

### docs/CONTRIBUTING.md

```markdown
# Contributing Guidelines

## How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Code Standards

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write unit tests for new features

## Commit Messages

Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code refactoring
- `test:` Testing
```

### docs/API.md

```markdown
# API Documentation

## Endpoints

### Products

#### GET /products
Get all products for current business

**Response:**
```json
{
  "products": [
    {
      "id": "123",
      "name": "Product Name",
      "current_stock": 50
    }
  ]
}
```

[Add all other endpoints]
```

## Benefits of This Structure

1. **Organization**: Clear separation of concerns
2. **Maintainability**: Easy to update individual sections
3. **Discoverability**: Quick links to specific documentation
4. **Professional**: Standard structure recognized by developers
5. **Scalability**: Easy to add new documentation as project grows
6. **Version Control**: Better Git history for documentation changes

## Next Steps

1. Create the folder structure
2. Move existing files
3. Update all internal links
4. Add missing documentation (API, CONTRIBUTING)
5. Update image paths in all documents
6. Test all links work correctly

This structure follows industry best practices and makes your project more professional and accessible to contributors.

