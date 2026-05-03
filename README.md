# FastAPI Dev Notes

A hands-on learning repository covering the FastAPI User Guide from start to finish, with practical code examples and a SvelteKit frontend playground.

## Structure

```
FA-Dev-Notes/
├── src/
│   ├── user_guide/          # FastAPI User Guide examples
│   │   ├── dependencies/    # Dependency injection patterns
│   │   ├── security/        # OAuth2, JWT, password hashing
│   │   ├── sql_app/         # SQLModel + SQLAlchemy database integration
│   │   ├── sub_app/         # Bigger applications with routers
│   │   ├── static/          # Static file serving
│   │   └── test/            # Testing with pytest
│   └── adv_user_guide/      # Advanced User Guide examples
└── fast-api-frontend/       # SvelteKit frontend (Svelte 5)
```

## Topics Covered

- Path & query parameters, request body, response models
- Cookie, header, and query parameter models
- Form data, file uploads, and multipart
- Body fields, extra data types, JSON compatible encoder
- Handling errors and custom exception handlers
- Dependencies — functions, classes, sub-dependencies, yield, global
- Security — OAuth2 with Password + Bearer, JWT tokens, bcrypt hashing
- Middleware and CORS
- SQL database with SQLModel & SQLAlchemy (SQLite)
- Bigger applications — routers, sub-applications
- Background tasks
- Static files, metadata, and docs URL configuration
- Testing with pytest and the TestClient

## Setup

**Backend**

```bash
pip install -r requirements.txt
```

Run any example with uvicorn, e.g.:

```bash
uvicorn src.user_guide.user-guide:app --reload
```

**Frontend**

```bash
cd fast-api-frontend
npm install
npm run dev
```

## Requirements

- Python 3.10+
- Node.js 18+
