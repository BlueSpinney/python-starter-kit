p = [[0,0,0,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],]


class a_start():
    def __init__(self,gmap):
        self.gmap = gmap
    
    def start(self):
        nul = 0
        
        for i in range(len(self.gmap)):
            st = self.gmap[i]
            for b in range(len(st)):
                if st[b] == 0:
                    nul += 1
        print(nul)

#p1 = a_start(p)
#p1.start()
