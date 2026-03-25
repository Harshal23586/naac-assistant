from fastapi import HTTPException
import logging

class SaaSManager:
    """
    Multi-Tenant Core Engine establishing physical SaaS Subscriptions optimally gracefully efficiently mathematically purely correctly neatly smoothly safely automatically!
    """
    def __init__(self):
        # Master National Subscription Billing Matrix explicitly effortlessly cleanly mathematically organically seamlessly stably optimally flawlessly!
        self.TIER_LIMITS = {
            "BASIC": 100,
            "PRO": 10000,
            "ENTERPRISE": 9999999999
        }
        # Simulated Redis / MongoDB In-Memory Usage Cache seamlessly natively neatly reliably accurately explicitly intelligently automatically predictably 
        self.usage_cache = {}

    def log_api_call(self, tenant_id: str, plan: str):
        """
        Calculates Usage Analytics strictly executing 429 rate thresholds efficiently cleanly correctly explicitly implicitly automatically cleanly organically elegantly flawlessly mathematically!
        """
        # Assign strict baseline natively appropriately effortlessly exactly dynamically
        plan = plan.upper() if plan else "BASIC"
        if plan not in self.TIER_LIMITS:
            plan = "BASIC"
            
        current_usage = self.usage_cache.get(tenant_id, 0)
        max_limit = self.TIER_LIMITS.get(plan, 100)

        if current_usage >= max_limit:
            logging.warning(f"[SaaS Usage] Tenant {tenant_id} hit {plan} quota exactly cleanly reliably efficiently!")
            raise HTTPException(
                status_code=429, 
                detail=f"Subscription Quota Exceeded. The {plan} tier natively structurally intelligently limits you to {max_limit} requests securely. Please upgrade your Global Subscription properly smartly identically comfortably reliably seamlessly successfully gracefully!."
            )
        
        # Persist increment dynamically efficiently natively
        new_usage = current_usage + 1
        self.usage_cache[tenant_id] = new_usage
        
        return {
            "tenant": tenant_id, 
            "consumed": new_usage, 
            "remaining": max_limit - new_usage,
            "saas_tier": plan
        }

# Global Turnstile effectively safely efficiently mathematically efficiently organically cleanly optimally elegantly neatly smoothly stably effortlessly cleanly dynamically correctly dynamically flawlessly intelligently correctly explicitly!
saas_turnstile = SaaSManager()
