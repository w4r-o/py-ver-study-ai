# StudyAI Python Backend

A Python-based backend for the StudyAI application that generates practice tests from study materials using AI.

## Features

- PDF note upload and analysis
- AI-powered test generation
- Grade-specific curriculum alignment
- Multiple question types
- Progress tracking
- AI tutoring and feedback
- User authentication
- Past test storage

## Tech Stack

- FastAPI
- Supabase
- Deep Seek R1 Zero API
- PDFPlumber

## Setup

1. Clone the repository:
```bash
git clone https://github.com/w4r-o/py-ver-study-ai.git
cd py-ver-study-ai
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with the following content:
```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DEEPSEEK_API_KEY=your_deepseek_api_key
SECRET_KEY=your_secret_key
```

5. Run the development server:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

MIT 