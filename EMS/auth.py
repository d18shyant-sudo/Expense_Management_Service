import jwt

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/login"
)


SECRET_KEY = "secret_key"


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
def require_role(*required_role: str):

    def role_checker(
        user = Depends(get_current_user)
    ):

        if user["role"] not in required_role:

            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )

        return user

    return role_checker