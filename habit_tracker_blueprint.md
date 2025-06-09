# Habit Tracker – Detailed Development Blueprint & LLM Code‑Gen Prompts

> **Purpose:** Provide a granular, test‑driven roadmap that a developer (or an LLM) can follow step‑by‑step. Each iteration is small, safe, and fully tested, yet pushes the project forward. Prompts are included at the end, ready to feed into a code‑generation LLM.

---

## 1. High‑Level Phases
| Phase | Goal | Deliverable |
|-------|------|-------------|
| 0 | Project bootstrap & CI | Git repo, Dockerfile, CI pipeline running tests |
| 1 | Core backend models & API | FastAPI app with Habit & Entry endpoints + unit tests |
| 2 | Frontend skeleton & data fetching | Next.js app fetching `/habits` & `/entries` |
| 3 | Habit CRUD UI | Settings page to add/edit/delete habits |
| 4 | Entry logging UI | Week grid (desktop) + day form (mobile) |
| 5 | Rule evaluation engine | Service that colors cells & computes success |
| 6 | Weekly summary sidebar | Stats & formatting on desktop |
| 7 | Mobile optimizations | Responsive tweaks & day view UX |
| 8 | Category management & filters | Create categories, filter grid |
| 9 | Security & deployment | Token auth, HTTPS, AWS infra |

---

## 2. Iteration Breakdown (Chunk → Steps)
Below, each **chunk** equals one short PR / LLM prompt cycle. Steps are atomic, testable actions.

### Phase 0 – Bootstrap & CI
**Chunk 0.1 – Repo & Tooling**  
1. Init Git repo (`git init`, `.gitignore`)  
2. Add `README.md` with project intro  
3. Commit skeleton

**Chunk 0.2 – Python env**  
1. Create `pyproject.toml` (Poetry)  
2. Add `fastapi`, `pydantic`, `uvicorn`, `pytest`  
3. Add `scripts/` for tooling

**Chunk 0.3 – Node env**  
1. `npm init -y` in `frontend/`  
2. Install `next`, `react`, `jest`, `testing-library`  
3. Commit lockfiles

**Chunk 0.4 – Docker & CI**  
1. Write backend `Dockerfile`  
2. Write frontend `Dockerfile`  
3. Add GitHub Actions workflow: lint → test → build  
4. Verify CI passes

---

### Phase 1 – Backend Core API
**Chunk 1.1 – FastAPI skeleton**  
1. Create `app/main.py` with `/health` route  
2. Add pytest health test

**Chunk 1.2 – Data models**  
1. Define `Habit`, `Entry` Pydantic models  
2. Write unit tests for model validation

**Chunk 1.3 – In‑memory storage**  
1. Service layer with dict storage  
2. CRUD methods for habits & entries  
3. Tests covering CRUD paths

**Chunk 1.4 – REST endpoints**  
1. `/habits/*` routes wired to service  
2. `/entries/*` routes wired to service  
3. 100 % test coverage of happy + error cases

**Chunk 1.5 – OpenAPI & docs**  
1. Enable FastAPI docs  
2. Add examples & schemas  
3. Snapshot tests to assert schema changes

---

### Phase 2 – Frontend Skeleton
**Chunk 2.1 – Next.js bootstrap**  
1. Create `pages/index.tsx` with placeholder  
2. Add Jest smoke test

**Chunk 2.2 – API client**  
1. `lib/api.ts` using Fetch  
2. Unit test with MSW mocking

**Chunk 2.3 – SWR data hook**  
1. `useHabits`, `useEntries` hooks  
2. Tests for hook caching

---

### Phase 3 – Habit CRUD UI
**Chunk 3.1 – Settings route**  
1. `pages/settings.tsx`  
2. Link from navbar

**Chunk 3.2 – HabitForm component**  
1. Controlled form w/ validation (React Hook Form + Zod)  
2. Jest + Testing Library unit tests

**Chunk 3.3 – Habit list & delete**  
1. Table of existing habits  
2. Delete button w/ confirm  
3. Tests for optimistic updates

---

### Phase 4 – Entry Logging UI
**Chunk 4.1 – Week grid skeleton (desktop)**  
1. Layout rows × cols  
2. Snapshot test responsive grid

**Chunk 4.2 – Cell input types**  
1. Toggle for binary  
2. Stepper for numeric  
3. Dropdown for categorical  
4. Tests on input render per type

**Chunk 4.3 – Day form (mobile)**  
1. Media query to switch layout  
2. Re‑use Cell inputs in stacked list

---

### Phase 5 – Rule Evaluation Engine
**Chunk 5.1 – Rule evaluator lib**  
1. Functions for `is_done`, `>=`, `==`, `value in`  
2. Unit tests covering all rule combos

**Chunk 5.2 – Daily color logic**  
1. API returns `status` per entry  
2. Grid cell uses status class  
3. Snapshot tests for styles

**Chunk 5.3 – Weekly summary calc**  
1. Helper to aggregate entry set  
2. Tests for `days_met`, `sum >=`, `average >=`, `at least one`

---

### Phase 6 – Weekly Summary Sidebar
**Chunk 6.1 – Stats component**  
1. Show % success, totals  
2. Unit test calculation edge cases

**Chunk 6.2 – Sidebar layout & styling**  
1. Sticky sidebar  
2. Responsive hide on mobile  
3. Snapshot tests

---

### Phase 7 – Mobile Optimizations
**Chunk 7.1 – Touch input polish**  
1. Larger hit zones  
2. Scroll‑lock fixes

**Chunk 7.2 – PWA install hint**  
1. Add manifest  
2. Lighthouse test score ≥ 90

---

### Phase 8 – Category Management & Filters
**Chunk 8.1 – Category CRUD UI**  
1. Form + list  
2. Tests

**Chunk 8.2 – Grid filter by category**  
1. Multi‑select filter  
2. Tests for filtered query

---

### Phase 9 – Security & Deployment
**Chunk 9.1 – Token auth middleware**  
1. Verify header  
2. Integration tests

**Chunk 9.2 – HTTPS & CORS**  
1. TLS termination config  
2. Test local HTTPS

**Chunk 9.3 – AWS IaC (Terraform)**  
1. Define RDS, ECS/Lambda, S3  
2. CI deploy stage

**Chunk 9.4 – E2E smoke tests**  
1. Playwright script hitting live URL  
2. Gate deploy on pass

---

## 3. Fine‑Grained Step “Right‑Sizing” Check
* Each chunk ≤ ~4 hours dev time  
* All new logic covered by automated tests  
* Frontend & backend cycle in lock‑step → no orphan routes/UI  
* CI always green before next chunk

---

## 4. LLM Code‑Generation Prompts
> Feed each prompt to your code‑gen model (e.g. GPT‑4) sequentially. Prompts are self‑contained and TDD‑oriented.

### Prompt 0.1 – Init Repo & README
```text
You are ChatGPT, acting as a professional dev. Create a new Git repo named "habit-tracker". Add a standard Python `.gitignore`, an MIT `LICENSE`, and a `README.md` with project overview, architecture summary, and build instructions. No code yet. Provide shell commands and file contents. Write unit tests = 0 (none). Return git diff format.
```

### Prompt 0.2 – Setup Python Environment
```text
Add `pyproject.toml` managed by Poetry. Dependencies: fastapi, uvicorn[standard], pydantic, pytest. Dev-dependencies: black, isort, pytest-cov. Provide `scripts/format.sh` to autoformat. Update README with install steps. Add CI workflow `.github/workflows/ci.yml` that installs, formats, and runs tests. Return git diff.
```

### Prompt 0.3 – Setup Node Environment
```text
Inside `frontend/`, initialize a Next.js TypeScript project (`13.x`). Install jest, @testing-library/react, @testing-library/jest-dom. Create jest config and a sample test that renders <div>Hello</div>. Update root README with frontend dev instructions. Provide git diff.
```

### Prompt 1.1 – FastAPI Skeleton & Health Route
```text
Add `app/main.py` with FastAPI instance and `/health` GET returning `{status: 'ok'}`. Add pytest `tests/test_health.py` hitting TestClient. Update CI to run backend tests. Ensure 100% passing. Output git diff.
```

### Prompt 1.2 – Core Models & Validation
```text
Create `app/models.py` defining Pydantic `Habit` and `Entry` as in spec. Include type enums and rule sub-models. Write unit tests covering model validation edge cases (missing fields, wrong types). Keep coverage ≥90%. Provide git diff.
```

### Prompt 1.3 – In-Memory Storage Service
```text
Implement `app/services.py` with `HabitService` & `EntryService` using dicts. Provide CRUD methods. Add tests for create/read/update/delete + failure paths (duplicate IDs, not found). Ensure 100% branch coverage. Git diff output.
```