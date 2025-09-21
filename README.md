# AI Humanizer - Transform Your Text with AI

A powerful Django web application that uses OpenAI's GPT-3.5-turbo to transform text into different styles and tones. Perfect for content creators, writers, marketers, and anyone who needs to adapt their text for different audiences.

## 🌟 Features

### 🤖 AI-Powered Text Transformation
- **Academic Style**: Formal, scholarly writing with proper vocabulary
- **Casual Tone**: Relaxed, conversational language
- **Emotional Expression**: Vivid, descriptive language that evokes feelings
- **Marketing Copy**: Persuasive content with power words and calls-to-action
- **Storytelling**: Engaging narrative with descriptive details
- **Simplified Text**: Clear, accessible language for general audiences

### 🌍 Multilingual Support
- **English (EN)** - Default language
- **Russian (RU)** - Русский интерфейс
- **Uzbek (UZ)** - O'zbek tilida interfeys

### 📊 Session-Based User Management
- Automatic user creation based on browser sessions
- Persistent history across page refreshes
- User activity tracking and analytics

### 💾 Database Integration
- All requests saved to PostgreSQL/SQLite database
- Processing time tracking for performance monitoring
- Admin interface for data management
- Automatic cleanup of old data

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 5.2+
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Humanizer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser**
   Navigate to `http://localhost:8000`

## 🛠️ Configuration

### Environment Variables
```bash
# Required
OPENAI_API_KEY=your-openai-api-key

# Optional
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

### Settings
The application uses Django's default settings with the following customizations:
- Static files configuration
- Media files handling
- Session management
- OpenAI integration

## 📁 Project Structure

```
AI-Humanizer/
├── app/
│   ├── models.py          # User and Request models
│   ├── views.py           # API endpoints
│   ├── openai.py          # OpenAI integration
│   ├── utils.py           # Prompt templates
│   ├── admin.py           # Admin interface
│   └── management/        # Custom commands
├── config/
│   ├── settings.py        # Django settings
│   └── urls.py           # URL configuration
├── templates/
│   └── index.html         # Main frontend
├── static/               # Static files
├── media/                # Media files
└── requirements.txt      # Dependencies
```

## 🔧 API Endpoints

### POST `/api/humanize/`
Transform text using AI
```json
{
    "text": "Your text here",
    "mode": "casual"
}
```

**Response:**
```json
{
    "original_text": "Your text here",
    "humanized_text": "Hey! So your text here",
    "mode": "casual",
    "processing_time": 1.23
}
```

### GET `/api/history/`
Get user's recent history
```json
{
    "history": [
        {
            "original_text": "Sample text",
            "humanized_text": "Transformed text",
            "mode": "academic",
            "timestamp": 1640995200,
            "created_at": "2022-01-01T00:00:00Z"
        }
    ]
}
```

## 🎨 Frontend Features

### Interactive Interface
- **Real-time text transformation** with typewriter effect
- **Language switching** without page reload
- **Sample text** for each mode
- **History management** with click-to-restore
- **Responsive design** for all devices

### User Experience
- **Loading states** with visual feedback
- **Error handling** with user-friendly messages
- **Copy functionality** for results
- **Smooth animations** and transitions

## 🗄️ Database Models

### User Model
```python
class User(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
```

### Request Model
```python
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text = models.TextField()
    humanized_text = models.TextField()
    mode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    processing_time = models.FloatField(null=True, blank=True)
```

## 🔧 Management Commands

### Cleanup Old Data
```bash
# Remove data older than 30 days
python manage.py cleanup_old_data

# Remove data older than 7 days
python manage.py cleanup_old_data --days 7

# Preview what would be deleted
python manage.py cleanup_old_data --dry-run
```

## 🚀 Deployment

### Production Settings
1. Set `DEBUG=False`
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure environment variables
5. Set up SSL/HTTPS

### Docker Deployment (Optional)
```dockerfile
FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 📊 Monitoring & Analytics

### Admin Interface
- Access at `/admin/` with superuser credentials
- View user activity and request statistics
- Monitor processing times and performance
- Search and filter data

### Key Metrics
- Total users and requests
- Average processing time
- Most popular transformation modes
- User activity patterns

## 🛡️ Security Features

- **CSRF protection** for all forms
- **Session-based** user identification
- **Input validation** and sanitization
- **Error handling** without data exposure
- **Rate limiting** (can be added)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

### Common Issues

**OpenAI API Errors:**
- Check your API key is valid
- Ensure you have sufficient credits
- Verify the API key is set in environment variables

**Database Issues:**
- Run `python manage.py migrate`
- Check database permissions
- Verify database connection settings

**Static Files Not Loading:**
- Run `python manage.py collectstatic`
- Check static file configuration
- Verify file permissions

### Getting Help
- Check the Django documentation
- Review OpenAI API documentation
- Open an issue on GitHub
- Contact the development team

## 🔮 Future Enhancements

- [ ] User authentication system
- [ ] Custom prompt templates
- [ ] Batch text processing
- [ ] Export functionality
- [ ] Advanced analytics dashboard
- [ ] API rate limiting
- [ ] Caching system
- [ ] Multi-language text support

---

**Made with ❤️ using Django and OpenAI**