class BinarySearch:


    def binary_s(self,l,search_value):
        l.sort()
        print(l)
        n = len(l)
        left,right = 0, n-1

        while left <= right:
            middle = (left+right)//2
            if search_value == l[middle]:
                print(l[middle],f"index : {middle}")
                break
            elif search_value < l[middle]:
                right = middle-1
            elif search_value > l[middle]:
                left = middle+1
        else:
            raise ValueError('Not Found')




b = BinarySearch()

b.binary_s([2,3,4,5,9,8,7,6,5,4,2,3,4],2)
