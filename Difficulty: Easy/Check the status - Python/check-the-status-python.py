class Solution:
    def checkStatus(self, a, b, flag):
        if flag == False and ((a >= 0) ^ (b >= 0)):
            # Condition 1: Exactly one of a or b is non-negative, flag is False
            return True
        if flag == True and (a < 0 and b < 0):
            # Condition 2: Both a and b are negative, flag is True
            return True
        # Otherwise
        return False
