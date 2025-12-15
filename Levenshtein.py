import numpy as np
import time
def minimum(a,b,c):
    if a<=b and a<=c:
        return a
    if b<=a and b<=c:
        return b
    if c<=a and c<=b:
        return c

def maximum(a,b):
    if a<b:
        return b
    else:
        return a

def LevenshteinDistance(A,B):
    K = np.zeros((len(A)+1, len(B)+1))    #A+1 x B+1 matrix   
    A_len= len(A)                                                        
    B_len= len(B)

    for i in range(1,A_len+1):
        K[i][0] = i
    for i in range(1,B_len+1):
        K[0][i] = i

    erase = 0
    add = 0
    replace = 0

    for i in range(1, A_len + 1):
        for j in range(1, B_len + 1):
            if A[i-1] == B[j-1]:
                K[i][j] = K[i-1][j-1]
            else:
                erase = K[i-1][j] + 1
                add = K[i][j-1] + 1
                replace = K[i-1][j-1] + 1
                K[i][j] = minimum(erase,add,replace) 

    return K[A_len][B_len]     #Returns end of the matrix so exactly Levenshtein Distance

print("This is a mini program to find Levenshtein Distance or Similarity Rate between two strings.\n")

while True:     #Mini Menu
    print("1 - for Levenshtein Distance \n2 - for Levenshtein Similarity Rate\n3 - for close")
    try:
        v = int(input())
            
        if v == 1:
            print("1. First Word:")
            word_1 = input()
            print("2. Second Word:")
            word_2 = input()

            Lev_Dis = LevenshteinDistance(word_1,word_2)
            print(Lev_Dis)
            time.sleep(4)
        elif v == 2:
            print("1. First Word:")
            word_1 = input()
            print("2. Second Word:")
            word_2 = input()

            Lev_Dis = LevenshteinDistance(word_1,word_2)
            max_len = maximum(len(word_1),len(word_2))
            similarity_rate = (max_len - Lev_Dis)/max_len
            print(similarity_rate)
            time.sleep(4)
        elif v == 3:
            break
        else:
            print("Just 1 2 3 :|")
    except Exception as e:
        print("Need int..")


        