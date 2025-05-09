# YouTube Blog Generator

A web application that converts YouTube videos into well-structured blog posts using AI. The application uses LangChain and Claude 3 Opus to generate high-quality content from video transcripts.

## Project Structure

```
youtube-blog-generator/
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── api/      # API routes
│   │   ├── core/     # Core configuration
│   │   ├── models/   # Data models
│   │   └── services/ # Business logic
│   └── requirements.txt
└── frontend/         # Next.js frontend
    ├── app/
    │   ├── components/
    │   └── page.tsx
    └── package.json
```

## Features

- Convert YouTube videos to blog posts
- Generate SEO-optimized titles and meta descriptions
- Embed original video in the blog post
- Clean and modern user interface
- Real-time generation with progress feedback

## Setup

### Backend

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

5. Run the development server:
```bash
uvicorn app.main:app --reload
```

### Frontend

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

## Usage

1. Open `http://localhost:3000` in your browser
2. Enter a YouTube video URL
3. Click "Generate Blog Post"
4. Wait for the generation to complete
5. View and copy the generated blog post

## Technologies Used

- Backend:
  - FastAPI
  - LangChain
  - Claude 3 Opus
  - YouTube Transcript API

- Frontend:
  - Next.js 14
  - TypeScript
  - Tailwind CSS
  - React

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 