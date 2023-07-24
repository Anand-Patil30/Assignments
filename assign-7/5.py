def Three_Sum_Finder(arr, n):
    res = False
    Zero_Sum_List=[]
    List_of_List=[]
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    Zero_Sum_List = [arr[i], arr[j], arr[k]]
                    List_of_List.append(Zero_Sum_List)
                    res = True              
    if (res == False):
        print(" not exist ")
    else:
        print(List_of_List)    


Sample_list = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(Sample_list)
Three_Sum_Finder(Sample_list, n)
