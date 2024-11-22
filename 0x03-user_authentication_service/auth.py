#!/usr/bin/env python3
"""
auth.py
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
from typing import Union


def _hash_password(password: str) -> bytes:
    """
    hashes a password
    """
    encoded = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(encoded, salt)
    return hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """
        Save a user to a database with a password
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError('User {} already exists'.format(email))

    def valid_login(email: str, password: str) -> bool:
        """
        Authenticate a user to login
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
