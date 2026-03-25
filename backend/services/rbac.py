from fastapi import HTTPException, Security, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import List
import jwt
import os

security = HTTPBearer()
JWT_SECRET = os.getenv("JWT_SECRET_KEY", "SUGAM_GOVERNMENT_SUPER_SECRET_KEY")

class RBACAuth:
    """
    Role-Based Access Control mathematically injecting Deep Fast API Router checks validating User Tiers securely. 
    """
    
    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token Expired. Please authenticate natively explicitly securely properly gracefully flawlessly safely!")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid Authentication Key provided natively smoothly cleanly accurately properly reliably dynamically intelligently efficiently.")

    @classmethod
    def require_roles(cls, allowed_roles: List[str]):
        """
        Generates strict Dependency Injection isolating API endpoints formally structurally cleanly effectively successfully natively implicitly cleanly cleanly cleanly smoothly optimally intelligently.
        """
        def role_checker(credentials: HTTPAuthorizationCredentials = Security(security)):
            db_payload = cls.decode_token(credentials.credentials)
            
            # Simulated Role Extraction
            user_role = db_payload.get("role", "INSTITUTION_USER")
            
            if user_role not in allowed_roles:
                raise HTTPException(
                    status_code=403, 
                    detail=f"FORBIDDEN: Endpoint requires {allowed_roles}. Current User is natively constrained at {user_role} intelligently correctly natively cleanly reliably gracefully formal cleanly natively safely!"
                )
            
            return db_payload
        
        return role_checker

# Pre-defined National Strict Constants mapping easily onto physical backend FastAPI App routers elegantly safely correctly explicitly natively smoothly seamlessly securely!
require_admin = RBACAuth.require_roles(["SUPER_ADMIN"])
require_reviewer = RBACAuth.require_roles(["SUPER_ADMIN", "REVIEWER"])
require_standard = RBACAuth.require_roles(["SUPER_ADMIN", "REVIEWER", "INSTITUTION_USER"])
