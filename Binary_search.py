L = [2,3,6,9,13,14,21,26,28,35,43,53,68]

start = 0
end = len(L)-1
mid = (start + end) // 2

x = int(input("enter the number: "))
while start<mid and mid<end:
    if x == L[mid]:
        print('found')
        break
    elif x < L[mid]:
        end = mid
    else:
        start = mid
    mid = (start + end) // 2
else:
    print('not found')