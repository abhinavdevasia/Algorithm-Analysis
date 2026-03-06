import random
import time

def insertion_sort(ls):
    n=len(ls)
    for i in range(1,n):
        key=ls[i]
        j=i-1
        while j>=0 and key<ls[j]:
            ls[j+1]=ls[j]
            j-=1
        ls[j+1]=key


def best_test_case(n):
    return list(range(1,n+1))

def worst_test_case(n):
    return list(range(n,0,-1))

def avg_test_case(n):
    arr=[random.randint(1,n) for i in range(n)]
    return arr

with open("insertion_sort_analysis.txt","w") as f:
    f.write("Insertion Sort Empirical Analysis\n\n")
    f.write(f"|{'Input size(n)':<15} | {'Best':<10} | {'Average':<12} | {'Worst':<10}|\n")
    f.write("-"*58+"\n")
    for n in [100,1000,2000,4000,8000]:
        start=time.perf_counter()
        insertion_sort(best_test_case(n))
        end=time.perf_counter()
        best_time=end-start

        start=time.perf_counter()
        insertion_sort(avg_test_case(n))
        end=time.perf_counter()
        avg_time=end-start
        
        start=time.perf_counter()
        insertion_sort(worst_test_case(n))
        end=time.perf_counter()
        worst_time=end-start
        f.write(f"|{n:<15} | {best_time:<10.6f} | {avg_time:<12.6f} | {worst_time:<10.6f}|\n")