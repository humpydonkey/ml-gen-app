#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="cyz19892002@gmail.com",
            password="asdf1234",
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser cyz19892002@gmail.com")
    init()
    print("Superuser created")
