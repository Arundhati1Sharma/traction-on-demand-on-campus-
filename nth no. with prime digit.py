def nthNumberWithPrimeDigit(n):
    l=[]
    lene = 1;
    prev_count = 0; 
    while(1):
        curr_count = (prev_count + 
                      math.pow(4, lene));
        if (prev_count < n and 
            curr_count >= n): 
            break; 
        lene += 1; 
    
  
        prev_count = curr_count;
    for i in range (1, lene + 1):
        for j in range(1, 5):
            if (prev_count + pow(4, lene - i) < n): 
                prev_count += pow(4, lene - i);
            else: 
                if (j == 1): 
                    l.append(2);
                elif (j == 2): 
                    l.append(3); 
                elif (j == 3): 
                    l.append(5); 
                elif (j == 4): 
                    l.append(7); 
                break; 
    new=""
    for i in range(len(l)):
        new+=str(l[i])           
    return (int(new));
