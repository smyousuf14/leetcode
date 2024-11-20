class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        stringN = str(n)
        sumTotal = 0
        processOver = False
        
        while not processOver:
            for char in stringN:
                sumTotal = sumTotal + pow(int(char), 2)
                print(sumTotal)
            
            if sumTotal == 1 or (len(str(sumTotal)) == 1):
                processOver = True
            else:
                stringN = str(sumTotal)
                print(sumTotal)
                sumTotal = 0

        print(sumTotal)
        if sumTotal == 1 or sumTotal == 7:
            return True
        else:  
            return False