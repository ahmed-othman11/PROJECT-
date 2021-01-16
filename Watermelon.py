*********************
* 3 way to solve :) *
*********************

w = int(input())
if w >= 4:
    if w % 2 == 0:
        print('YES') 
    else:
        print('NO')
else:
    print('NO')
    
---------------------------
def watermelon():
    w = int(input())
    if w >= 4:
        if w % 2 == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
 
 
print(watermelon())
------------------------
class water():
    def watermelon(self):
        w = int(input())
        if w >= 4:
            if w % 2 == 0:
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
 
water_melon = water()
print(water_melon.watermelon())
