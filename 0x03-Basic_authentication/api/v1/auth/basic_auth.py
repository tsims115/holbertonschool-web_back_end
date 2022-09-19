#!/usr/bin/env python3
"""basic auth module None for now"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth Class that is None for now"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ return Base64 part of auth_header """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if "Basic " in authorization_header:
            return authorization_header[6:]
        return None
