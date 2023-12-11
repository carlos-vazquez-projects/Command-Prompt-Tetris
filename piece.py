#By Carlos Vazquez on 11-17-22

class Piece():
  def __init__(self,n,x):
    self.name = n
    self.coords = x
    self.orientation = 1

  def return_decor_coords(self):
    if(self.name[0] == 'O'):
      return [[0,0],[0,1],[1,0],[1,1]]
    elif(self.name[0] == 'Z'):
      return [[0,0],[0,1],[1,1],[1,2]]
    elif(self.name[0] == 'S'):
      return [[0,1],[0,2],[1,0],[1,1]]
    elif(self.name[0] == 'T'):
      return [[0,1],[1,0],[1,1],[1,2]]
    elif(self.name[0] == 'I'):
      return [[0,0],[0,1],[0,2],[0,3]]
    elif(self.name[0] == 'J'):
      return [[0,0],[1,0],[1,1],[1,2]]
    elif(self.name[0] == 'L'):
      return [[1,0],[1,1],[1,2],[0,2]]
    
  def returnCoords(self):
    return self.coords
    
  def changeCoords(self, new):
    self.coords = [new[0], new[1], new[2], new[3]]
  
  def changePiece(self, n):
    self.name = n
    
  def lowestColumns(self):
    lowest = []
    cols = {}
    keys = []
    
    for i in self.coords:
      if(i[1] not in cols):
        cols[i[1]] = []
        keys.append(i[1])
    
    counter = 0
    for i in keys:
      for q in self.coords:
        if(q[1] == i):
          cols[i].append(q[0])
      counter += 1
    
    for i in keys:
      lowest.append((max(cols[i]), i))
    
    return lowest

    
  def __str__(self):
    return str(self.name) + ' piece, in orientation ' + str(self.orientation) + ' at the coordinates ' + str(self.coords)
