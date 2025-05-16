def find_square_root(n):

    l,r=0,n
    ans=-1

    while l<=r:
        mid=(l+r)//2
        if mid*mid==n:
            ans=mid
            r=mid-1
        elif mid*mid<n:
            l=mid+1
        else:
            r=mid-1
    return ans
# Example usage
if __name__ == "__main__":
    n = 16
    result = find_square_root(n)
    if result != -1:
        print(f"The square root of {n} is {result}.")
    else:
        print(f"{n} is not a perfect square.")
    n = 20
    result = find_square_root(n)
    if result != -1:
        print(f"The square root of {n} is {result}.")
    else:
        print(f"{n} is not a perfect square.")