class ladder:
    def __init__(self,words):
        self.graph = self.creategraph(words)
        print(self.graph)
    
    def creategraph(self,words):
        
        graph = {}
        
        for i in range(9):
            for j in range(9):
                word1 = words[i]
                word2 = words[j]
                
                if self.dif(word1,word2):
                    self.connection(word1,word2,graph)
                    
        return graph
                    
                    
    def dif(self,word1,word2):
        
        ctr= 0
        
        for i in range(4):
            if(word1[i]!=word2[i]):
                ctr+=1
                
        if ctr == 1:
            return True
        else:
            return False
    
    def connection(self,origin,dest,graph):
        if origin in graph.keys():
            if dest not in graph[origin]:
                graph[origin].append(dest)
                graph[origin].sort()
        else:
            graph[origin] = []
            
        if dest in graph.keys():
            if origin not in graph[dest]:
                graph[dest].append(origin)
                graph[dest].sort()
        else:
            graph[dest] = []

if __name__ == "__main__":
    words=["head","tead","heal","seal","feal","fell","fail","peal","fall"]
    x = ladder(words)
    


