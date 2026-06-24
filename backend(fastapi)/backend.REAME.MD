## Day wise progress

**Day 01** - commit: "make basic register route"
Made the first `POST /auth/register` route. Plain password, no hashing yet.

**Day 02** - commit: "password hashed and storage in database"
Added `pwdlib` and started hashing the password before saving it to DB.

**Day 03** - commit: "recall previous code and make basic login controller"
Wrote the first `login` controller — checks user by username, verifies password.

**Day 04** - commit: "make complete login api with jwt token"
Login now generates a JWT token (`jwt.encode`) and returns it, using settings from `.env`.

**Day 05** - commit: "make authenticated route"
Added an `is_auth` check — reads the token from the request header and verifies it.

**Day 06** - commit: "Secure Endpoints with Authentication"
Used `is_auth` as a dependency to protect routes, so only logged-in users can access them.

**Day 07** - commit: "Implement Table Relationships - One-to-Many in FastAPI & SQLAlchemy"
Linked `tasks` table to `users` table with a `ForeignKey(user_id)` — one user can have many tasks.

**Day 08** - commit: "practise authentication / authorization"
Cleaned up login/auth code, fixed status codes (401 for invalid password, 404 for user not found).

**Day 09** - commit: "practise protect route and more / implement table relationships"
Made login accept one `identifier` field (username or email both work), kept refining the task-user relation.

**Day 10** - commits: "add task CRUD with user authorization", "send a welcome message when user register", "email details like password/username/email add in .env file for security reason"
Task routes now require login (`Depends(is_auth)`) so each user only sees their own tasks. Register sends a welcome email automatically using FastAPI-Mail. Email password got committed to GitHub by mistake at first — had to revoke the Gmail app password, generate a new one, and move everything into `.env`.

## Folder structure

```
backend(fastapi)/
├── day-01/
├── day-02/
├── day-03/
├── day-04/
├── day-05/
├── day-06/
├── day-07/
├── day-08/
├── day-09/
└── day-10/
```

## Tech used

- FastAPI
- PostgreSQL + SQLAlchemy
- Alembic (migrations)
- pwdlib (password hashing)
- PyJWT (auth token)
- FastAPI-Mail (email)

## A few things I learned

- pwdlib is the best option for password hashing
- Keep the JWT in an httponly cookie, not a regular cookie
- Put .env in .gitignore from the start, adding it later doesn't help if it's already committed
- If a secret/password accidentally gets pushed, revoke it first, then clean up the history
- Alembic migrations make it much easier to track database changes
- `or_()` in SQLAlchemy is handy when login should accept either username or email
