
import random
import numpy as np
def main():
    t = int(input("Enter Sample data size : "))
    p = int(input("Enter number of Pigeon Hole: "))
    times(t,p)
    
def times(a = 1,pigeon_holes=10):
    sample_dict_list = []
    sample_dict={}
    pigeon_hole_num_sets = [[]]
    pigeon_hole_num = []
    pigeon_hole_num_sets.clear()
    list_hole_true = []
    random.seed()
    for i in range(0,a):
        flag = 0
        pigeon_hole_num.clear()
        
        for m in range(0,pigeon_holes+1):
            sample_dict[m] = 0
            
   
        random.seed()
        for j in range(0,int(pigeon_holes/2)):
            pigeon_hole_num.append(random.randint(1,pigeon_holes+1))
        pigeon_hole_num_sets.insert(i,pigeon_hole_num.copy())
        
        for l in range(0,pigeon_holes+1):
            for k in range(0,int(pigeon_holes/2)):
                if(pigeon_hole_num[k]==l):
                    sample_dict[l] = int(sample_dict[l]) + 1
            if(sample_dict[l] > 1 and flag == 0):
                list_hole_true.append(True)
                flag = 1
        sample_dict_list.append(sample_dict.copy())
        
    print(pigeon_hole_num_sets)
    print()
    print(sample_dict_list)
    print(len(list_hole_true))
    print((len(list_hole_true)/a) * 100)
main()
