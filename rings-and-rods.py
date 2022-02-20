class Solution:
    def countPoints(self, rings: str) -> int:
        rings = list(rings)
        ring = rings[::2]
        rod = rings[1::2]
        # print(ring,rod)
        gg = {}
        for i in range(len(rod)):
            
            try:

                if rod[i]  in gg.keys():
                    gg[rod[i]] +=(ring[i])
                else:
                    gg[rod[i]] = ring[i]
            except :
                continue
        num = 0
        for i in gg.keys():
            k = list(gg[i])
            print(k)
            if 'B' in k and 'G' in k and 'R' in k:
                num+=1
        print(gg)  
        return num
