import random 
def max_min(mlist):
    minimum =mlist[0]
    for num in mlist:
      if num<minimum:
         minimum=num

         return minimum
      
      def getValues():
         mlist = random .sample(range(1,30),5)
         print(mlist)
         result=max_min(mlist)
         print(result)
    print(f"value is {minimum}")


mlist = random.sample(range(1,30),5)
print(mlist)
max_min(mlist)