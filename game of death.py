def gameOfDeath(n, k): 
  
      if (n == 1): 
          return 1
      else:
          return (gameOfDeath(n - 1, k) + k-1) % n + 1
