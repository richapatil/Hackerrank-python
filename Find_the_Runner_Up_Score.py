n = int(input())
arr = map(int, input().split())

      # The set() function creates a set object which helps to store items in single variable. 
      # The items in a set list are unordered, so sorted function is applied to get ordered list 
      # and then second largest element is printed
      
print(sorted(list(set(arr)))[-2])
