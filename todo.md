# Habit Tracker Project Todo List

## Phase 0 - Bootstrap & CI
### Chunk 0.1 - Repo & Tooling
- [x] Initialize Git repository
- [x] Add .gitignore
- [x] Create README.md with project intro
- [x] Initial commit

### Chunk 0.2 - Python Environment
- [x] Create pyproject.toml (Poetry)
- [x] Add core dependencies (fastapi, pydantic, uvicorn, pytest)
- [x] Add development dependencies (black, isort, pytest-cov)
- [x] Create scripts/ directory for tooling

### Chunk 0.3 - Node Environment
- [x] Initialize Next.js TypeScript project in frontend/
- [x] Install core dependencies (next, react)
- [x] Install testing dependencies (jest, testing-library)
- [x] Set up Jest configuration
- [x] Create sample test

### Chunk 0.4 - Docker & CI
- [x] Create backend Dockerfile
- [x] Create frontend Dockerfile
- [x] Set up GitHub Actions workflow
- [x] Verify CI pipeline

## Phase 1 - Backend Core API
### Chunk 1.1 - FastAPI Skeleton
- [ ] Create app/main.py
- [ ] Implement /health route
- [ ] Write health endpoint tests

### Chunk 1.2 - Data Models
- [ ] Define Habit Pydantic model
- [ ] Define Entry Pydantic model
- [ ] Write model validation tests

### Chunk 1.3 - In-memory Storage
- [ ] Implement HabitService
- [ ] Implement EntryService
- [ ] Write CRUD operation tests

### Chunk 1.4 - REST Endpoints
- [ ] Implement /habits/* routes
- [ ] Implement /entries/* routes
- [ ] Write endpoint tests
- [ ] Achieve 100% test coverage

### Chunk 1.5 - OpenAPI & Docs
- [ ] Enable FastAPI docs
- [ ] Add API examples
- [ ] Add schema documentation
- [ ] Write schema snapshot tests

## Phase 2 - Frontend Skeleton
### Chunk 2.1 - Next.js Bootstrap
- [ ] Create pages/index.tsx
- [ ] Add basic layout
- [ ] Write smoke tests

### Chunk 2.2 - API Client
- [ ] Create lib/api.ts
- [ ] Implement API client methods
- [ ] Set up MSW for testing
- [ ] Write API client tests

### Chunk 2.3 - SWR Data Hooks
- [ ] Implement useHabits hook
- [ ] Implement useEntries hook
- [ ] Write hook tests

## Phase 3 - Habit CRUD UI
### Chunk 3.1 - Settings Route
- [ ] Create pages/settings.tsx
- [ ] Add navigation link

### Chunk 3.2 - HabitForm Component
- [ ] Create form component
- [ ] Add form validation
- [ ] Write form tests

### Chunk 3.3 - Habit List & Delete
- [ ] Create habit list component
- [ ] Add delete functionality
- [ ] Write list component tests

## Phase 4 - Entry Logging UI
### Chunk 4.1 - Week Grid Skeleton
- [ ] Create grid layout
- [ ] Add responsive design
- [ ] Write layout tests

### Chunk 4.2 - Cell Input Types
- [ ] Implement binary toggle
- [ ] Implement numeric stepper
- [ ] Implement categorical dropdown
- [ ] Write input type tests

### Chunk 4.3 - Day Form (Mobile)
- [ ] Create mobile layout
- [ ] Implement stacked list view
- [ ] Add responsive switching

## Phase 5 - Rule Evaluation Engine
### Chunk 5.1 - Rule Evaluator
- [ ] Implement rule evaluation functions
- [ ] Write rule combination tests

### Chunk 5.2 - Daily Color Logic
- [ ] Add status calculation
- [ ] Implement cell coloring
- [ ] Write style tests

### Chunk 5.3 - Weekly Summary
- [ ] Create summary calculation helpers
- [ ] Write summary tests

## Phase 6 - Weekly Summary Sidebar
### Chunk 6.1 - Stats Component
- [ ] Create stats display
- [ ] Add calculation logic
- [ ] Write stats tests

### Chunk 6.2 - Sidebar Layout
- [ ] Implement sticky sidebar
- [ ] Add responsive behavior
- [ ] Write layout tests

## Phase 7 - Mobile Optimizations
### Chunk 7.1 - Touch Input
- [ ] Optimize touch targets
- [ ] Fix scroll issues

### Chunk 7.2 - PWA Support
- [ ] Add web manifest
- [ ] Implement PWA features
- [ ] Run Lighthouse tests

## Phase 8 - Category Management
### Chunk 8.1 - Category CRUD
- [ ] Create category management UI
- [ ] Write category tests

### Chunk 8.2 - Grid Filtering
- [ ] Implement category filter
- [ ] Write filter tests

## Phase 9 - Security & Deployment
### Chunk 9.1 - Authentication
- [ ] Implement token auth
- [ ] Write auth tests

### Chunk 9.2 - HTTPS & CORS
- [ ] Configure TLS
- [ ] Set up CORS
- [ ] Test security features

### Chunk 9.3 - AWS Infrastructure
- [ ] Create Terraform configs
- [ ] Set up CI deployment

### Chunk 9.4 - E2E Testing
- [ ] Write Playwright tests
- [ ] Set up E2E test pipeline 