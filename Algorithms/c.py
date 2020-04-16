from collections import Counter
rem_tuples = []
n, k = list(map(int, input().split()))
distances = [0] + [None]*(n-1)
for _ in range(n-1):
    a, b = list(map(int, input().split()))

    if a==1: distances[b-1] = 1
    elif b==1: distances[a-1] = 1

    elif distances[a-1]!=None:
        if not distances[b-1]:
            distances[b-1] = distances[a-1] + 1
        else:
            distances[b-1] = min(distances[b-1], distances[a-1] + 1)

    elif distances[b-1]!=None:
        if not distances[a-1]:
            distances[a-1] = distances[b-1] + 1
        else:
            distances[a-1] = min(distances[a-1], distances[b-1] + 1)
    else:
        rem_tuples.append((a, b))
    
    # print(a, b, distances)



# print(rem_tuples)
# print(distances)
for tup in rem_tuples:
    a, b = tup

    if distances[a-1]!=None:
        if not distances[b-1]:
            distances[b-1] = distances[a-1] + 1
        else:
            distances[b-1] = min(distances[b-1], distances[a-1] + 1)

    elif distances[b-1]!=None:
        if not distances[a-1]:
            distances[a-1] = distances[b-1] + 1
        else:
            distances[a-1] = min(distances[a-1], distances[b-1] + 1)

distances = sorted(distances, reverse= True)
unique_distances = sorted(list(set(distances[:k])), reverse = True)
count = Counter(distances)

ans = 0
print(unique_distances, distances, count)
if k==1:
    ans = distances[0]

for i in range(len(unique_distances)-1):
    big = count[unique_distances[i]]
    small = count[unique_distances[i+1]]
    
    if i!=len(unique_distances)-2:
        ans += big*(unique_distances[i] - 1)
        k -= 1
    else:
        # i == len(unique_distances) - 1
        if k<=big:
            ans += k*unique_distances[i]
        elif k>big and k<=(small + big):
            small_left = (small + big) - k
            if small_left>=big:
                ans += big*unique_distances[i]
                ans += (k-big)*unique_distances[i+1]
                break
            elif small_left<big:
                ans += small_left*unique_distances[i]
                ans += (big - small_left)*(unique_distances[i] - 1)
                k = k - big
                ans += k*unique_distances[i+1]
                break
print(ans)

# for dist in distances:
    # print(count, unique)
    # if curr == dist and count!=unique-1:
    #     ans += (dist - 1)
    #     k -=1

    # elif curr!=dist:
    #     count += 1
    #     curr = dist
    #     if count!=unique - 1:
    #         ans += (dist - 1)
    #         k -=1

    # elif count == unique - 1:
        # Get the frequency of next element and curr element

# print(unique_dists, distances)
# for count in range(1, unique):
#     small = d[unique_dists[count]]
#     big = d[unique_dists[count-1]]

#     print(small, unique_dists[count], big, unique_dists[count-1], k)

#     if k<=big:
#         ans += big*(unique_dists[count-1])
#         break
#     elif k > big:
#         print(ans, k, small, big)

#         rem = small - big
#         ans += min(rem, big)*(unique_dists[count-1])
#         k = k - min(rem, big)

#         ans += k*(unique_dists[count])
#         break

# print(ans)

        

    


# ans = 0
# big, small = 0
# currbig = distances[0]
# currsmall = None
# for i in range(len(distances)):
#     if distances[i] == curr:
#         big += 1
#     else:
#         if currsmall is None:
#             currsmall = distances[i]
#             small += 1
#         elif distances[i] == currsmall:
#             small +=1
#         else:
#             if k < big:
#                 ans = k*curr
#                 break
#             elif big < k <
#             if rem == 0:
#                 k = k - (small + big)
#                 ans = currsmall*small + curr*big


#             curr = currsmall
#             currsmall = distances[i]
#             big = small
#             small = 1
            











