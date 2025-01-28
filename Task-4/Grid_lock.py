def readInts():return map(int,input().strip().split())

def make_sets(grid):
    rows=len(grid)
    cols=len(grid[0])
    word_slots=set()
    visited=set()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]!="-":continue
            if col==0 or grid[row][col-1]!="-":
                # right
                c=col
                while c<cols and grid[row][c]=="-":
                    visited.add((row,c))
                    c+=1
                if c-1>col:word_slots.add(((row,col),c-col,(0,1)))
            if row==0 or grid[row-1][col]!="-":
                # down
                r=row
                while r<rows and grid[r][col]=="-":
                    visited.add((r,col))
                    r+=1
                if r-1>row:word_slots.add(((row,col),r-row,(1,0)))
    return word_slots

def solve_sets(slots,words,used):
    def addt(a,b):
        ar,ac=a
        br,bc=b
        return (ar+br,ac+bc)

    if not words:return used

    word=words.pop()
    for (src,size,dd) in slots:
        if len(word)!=size:continue
        rc=src
        ok=True
        for d in range(size):
            if rc in used and used[rc]!=word[d]:
                ok=False
                break
            rc=addt(rc,dd)
        if not ok:continue
        used2=dict(used)
        rc=src
        for d in range(size):
            used2[rc]=word[d]
            rc=addt(rc,dd)
        slots2=set(slots)
        slots2.remove((src,size,dd))
        attempt=solve_sets(slots2,words,used2)
        if attempt:return attempt
    words.append(word)
    return None

grid=[input().strip() for _ in range(10)]
words=input().strip().split(";")
slots=make_sets(grid)
solution=solve_sets(slots,words,dict())
rows=len(grid)
cols=len(grid[0])

for row in range(rows):
    line=[]
    for col in range(cols):
        if (row,col) in solution:line.append(solution[(row,col)])
        else:line.append(grid[row][col])
    print("".join(line))
