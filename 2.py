import math
def allFactors(A):
        i = 1
        factors = []
        while i <= math.sqrt(A):
            if (A % i == 0) :
                if (A / i == i) :
                    factors.append(i)
                else :
                    factors.append(i)
                    factors.append(int(A/i))
            i = i + 1
        for i in range(0, len(factors)):    
            for j in range(i+1, len(factors)):    
                if(factors[i] > factors[j]):    
                    temp = factors[i];    
                    factors[i] = factors[j];    
                    factors[j] = temp; 
        return factors
print(allFactors(20))