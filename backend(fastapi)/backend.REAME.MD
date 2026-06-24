## Day wise progress

**Day 01** - Built basic CRUD for tasks (create, get all, get one, update, delete). Added a User model too.

**Day 02** - Cleaned up the task routes, better naming.

**Day 03** - Learned password hashing (using pwdlib) and started using JWT for register/login.

**Day 04** - Moved JWT secret key and algorithm into .env, stopped hardcoding them.

**Day 05** - Learned how to read and validate the JWT token from the request.

**Day 06** - Started storing the JWT in a cookie (httponly cookie) on login.

**Day 07** - Learned Alembic migrations, no longer depending on create_all().

**Day 08** - Cleaned up the auth flow a bit, used proper status codes (400, 401, 404).

**Day 09** - Made login work with either username or email, built the schema for it.

**Day 10** - Finalized register/login. On registration, the user now automatically gets a welcome email (used FastAPI-Mail). Kept the email credentials in .env. The password actually got leaked on GitHub once, so I revoked it and made a new one, and learned that secrets should never be hardcoded in code.

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
