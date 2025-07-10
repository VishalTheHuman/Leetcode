class Solution:
    global valid 
    valid = set(list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_"))
    global allowed_business
    allowed_business = set(["electronics", "grocery", "pharmacy", "restaurant"])

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def codeCheck(code): 
            if code == "" : 
                return False
            for c in code: 
                if c not in valid: 
                    return False
            return True
        
        def businessLineCheck(business):
            return business in allowed_business

        valid_coupons = []
        for idx in range(len(code)): 
            if isActive[idx] and \
            businessLineCheck(businessLine[idx]) and \
            codeCheck(code[idx]):
                valid_coupons.append((code[idx], businessLine[idx]))
        
        return [x[0] for x in sorted(valid_coupons, key = lambda x : (x[1], x[0]))]
