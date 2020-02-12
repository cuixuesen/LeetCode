import Queue
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i,j,grid):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j]="0"
            dfs(i-1,j,grid)
            dfs(i+1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)
            
        if len(grid) == 0:
            return 0
        
        island=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    island+=1                  
                    dfs(i,j,grid)       
        return island
   
        """       
        if len(grid) == 0:
            return 0
        i=0
        j=0
        rownum=len(grid)
        colnum=len(grid[0])
        print rownum,colnum
        q = Queue.Queue()
        islandnumber=0
        for row in range(rownum):
            for col in range(colnum):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    islandnumber +=1
                    q.put(colnum*row + col)
                    while not q.empty():
                        raw = q.get()
                        rawrow = int (raw / colnum)
                        rawcol = raw % colnum
                        print raw,rawrow,rawcol
                        if rawrow-1 >= 0 and grid[rawrow-1][rawcol]=="1":
                            grid[rawrow-1][rawcol]="0"
                            q.put((rawrow-1)*colnum + rawcol)
                        if rawrow+1 < rownum  and grid[rawrow + 1][rawcol]=="1":
                            grid[rawrow + 1][rawcol]="0"
                            q.put((rawrow + 1)*colnum + rawcol)
                            
                        if rawcol-1 >= 0 and grid[rawrow][rawcol-1]=="1":
                            grid[rawrow][rawcol-1]="0"
                            q.put(rawrow*colnum + rawcol-1)
                            
                        if rawcol+1 < colnum and grid[rawrow][rawcol+1]=="1":
                            grid[rawrow][rawcol+1]="0"
                            q.put(rawrow*colnum + rawcol+1)
                
        return islandnumber
        """
    