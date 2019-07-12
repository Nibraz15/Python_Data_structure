import math
import random
class watch():
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        time = []
        
        
        hr = 0
        minute = num
        
        while hr < 4 and minute >=0 :
            if minute > 5:
                hr = hr+1
                minute = minute -1
            else:
                
                hrli = self.hrlist(hr)
                
                minli=self.minlist(minute)
                
                
                for i in hrli:
                    for j in minli:
                        if len(str(j)) == 2:
                            time.append(str(i)+":"+str(j))
                        else:
                            time.append(str(i)+":0"+str(j))
                hr = hr+1
                minute = minute -1
                
        return time
                        
    
    def hrlist(self,hr):
        hrl=[]
        
        if hr==0:
            hrl.append(0)
        else:            
            permutaion = math.factorial(4) / ((math.factorial(4-hr))*(math.factorial(hr)))
            
            while permutaion > 0:
                i=0
                hrbin=[0,0,0,0]
                while i < hr:
                    rand = random.randint(0,3)
                    if hrbin[rand] != 1:
                        hrbin[rand] =1
                        i = i+1
                if self.binc(hrbin) not in hrl:
                    permutaion -= 1 
                    hrl.append(self.binc(hrbin))
        hrl.sort()
        for i in hrl:
            if (i) >= 12:
                hrl = hrl[:hrl.index(i)]
                break
        print hrl               
        return hrl

    def minlist(self,minute):
        minl=[]
        
        if minute == 0:
            minl.append(0)
        else:
            permutaion = math.factorial(6) / ((math.factorial(6-minute))*(math.factorial(minute)))
            
            while permutaion > 0:
                i=0
                minbin=[0,0,0,0,0,0]
                while i < minute:
                    rand = random.randint(0,5)
                    if minbin[rand] != 1:
                        minbin[rand] =1
                        i = i+1
                if self.binc(minbin) not in minl: 
                    permutaion -= 1
                    
                    
                    minl.append(self.binc(minbin))
        minl.sort()
        for i in minl:
            if (i) >= 60:
                minl = minl[:minl.index(i)]     
                break        
                        
                        
        return minl
    
    def binc(self,lis):
        val = 0
        for i in range(len(lis)):
            if lis[i] == 1:
                val = val + 2**i
        
        return val

lis= watch()
lis1 = lis.readBinaryWatch(3)

