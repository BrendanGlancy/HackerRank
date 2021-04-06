# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections


def main():
    # get the first line X which is the number of shoes
    x = int(input())
    
    # init earned 
    earned = 0
    
    # get the sizes avalible in the shop and assign it to a map
    sizes = collections.Counter(map(int, input().split()))
    
    # n represent the number of customers who want shoes, loop through and add
    # $ for the customers who qualify to buy shoes
    n = int(input())
    for i in range(n):
        # assign size and price to the remains lines in the input
        size, price = map(int, input().split())
        # remove the size from our sizes map and add price to earned
        # if the size is in our sizes list
        if size in sizes and sizes[size]:
            sizes[size] -= 1
            earned += price            
    
        
    print(earned)
    
main()
