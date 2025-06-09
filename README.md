# Habit Tracker

A modern, full-stack habit tracking application built with FastAPI and Next.js. Track your habits, visualize your progress, and build better routines.

## Features

- 📱 Responsive design for both desktop and mobile
- 📊 Visual habit tracking with weekly grid view
- 🎯 Customizable habit rules and goals
- 📈 Progress tracking and statistics
- 🔄 Real-time updates
- 🔒 Secure authentication
- 📱 PWA support for mobile devices

## Tech Stack

### Backend
- FastAPI (Python web framework)
- Pydantic (Data validation)
- Poetry (Dependency management)
- pytest (Testing)

### Frontend
- Next.js 13+ (React framework)
- TypeScript
- SWR (Data fetching)
- Jest & Testing Library (Testing)

### Infrastructure
- Docker
- GitHub Actions (CI/CD)
- AWS (Deployment)

## Project Structure

```
habit-tracker/
├── app/                    # Backend FastAPI application
│   ├── main.py            # FastAPI application entry
│   ├── models.py          # Pydantic models
│   └── services.py        # Business logic
├── frontend/              # Next.js frontend application
│   ├── pages/            # Next.js pages
│   ├── components/       # React components
│   └── lib/              # Utility functions
├── tests/                # Backend tests
├── scripts/              # Development scripts
└── docker/              # Docker configuration
```

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- Poetry
- Docker (optional)

### Backend Setup

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Run the development server:
```bash
poetry run uvicorn app.main:app --reload
```

### Frontend Setup

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

## Development

- Backend API will be available at `http://localhost:8000`
- Frontend will be available at `http://localhost:3000`
- API documentation will be available at `http://localhost:8000/docs`

## Testing

### Backend Tests
```bash
poetry run pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
