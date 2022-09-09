import numpy as np

def calculate(list):
  try:
    array = np.array(list).reshape(3, 3)
    
  except:
    raise ValueError('List must contain nine numbers.')
    
  calculations = {}
  
  calculations['mean'] = [
    array.mean(axis = 0).tolist(),
    array.mean(axis = 1).tolist(),
    array.mean()
  ]
    
  calculations['variance'] = [
    array.var(axis = 0).tolist(),
    array.var(axis = 1).tolist(),
    array.var()
  ]
    
  calculations['standard deviation'] = [
    array.std(axis = 0).tolist(),
    array.std(axis = 1).tolist(),
    array.std()
  ]
    
  calculations['max'] = [
    array.max(axis = 0).tolist(),
    array.max(axis = 1).tolist(),
    array.max()
  ]
    
  calculations["min"] = [
    array.min(axis = 0).tolist(),
    array.min(axis = 1).tolist(),
    array.min()
  ]

  calculations["sum"] = [
    array.sum(axis = 0).tolist(),
    array.sum(axis = 1).tolist(),
    array.sum()
  ]
    
  return calculations
