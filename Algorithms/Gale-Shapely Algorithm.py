# Also knows as the deferred acceptance algorithm.
# Helps in matching two groups in a 'greedy' manner to achieve a 'stable matching'.


## This implementation assumes each hospital can only make one candidate. Each candidate can only accept one offer. The number of hospitals is same as number of candidates. And each have provided a list of preferences for all belong to the other group (two groups: hospital and candidates)


# Hospital residency - Candidate matching.
from collections import deque, defaultdict

# Dictionary of hospitals and their preferences in queues. First in the queue is the first prefernce
H = {'Atlanta': deque(['Preeti', 'Ramon', 'Qi']), 'Boston': deque(['Preeti', 'Qi', 'Ramon']), 'Chicago': deque(['Preeti', 'Ramon', 'Qi'])}

# Dictionary of candidates and their preference order. (Candidate, Hospital pair.)
K = {('Preeti', 'Atlanta'): 3,('Preeti', 'Boston'): 1,('Preeti', 'Chicago'): 2 ,('Ramon', 'Atlanta'): 2,('Ramon', 'Boston'):3 ,('Ramon', 'Chicago'): 1,('Qi', 'Atlanta'): 3 , ('Qi', 'Boston'): 2,('Qi', 'Chicago'):1}

# Dictionary of Tentatively matched pairs. Stores the key as candidate full name and value as hospital preference order
T = {}

# Psuedocode
# while any hospital H has an opening and offers to make:
#     set K to current hospital's top remaining candidate
#     remove K from hospital's list of candidates

#     if current hospital (H) offer has higher preference than K's tentative holding:
#         reject K's tentative holding offer
#         set K's tentative holding offer to current hospital
#     else:
#         reject current hospitals (H) offer

# finalize tentative match

# If no candidate remains on hospital list, incremement counter
hospital_open_offer_indicator = len(H)
hospital_open_indicator = {'Atlanta':1, 'Boston':1, 'Chicago':1} # initially all are open

while sum(hospital_open_indicator.values())!=0 and hospital_open_offer_indicator != 0:
    # no opening left         # offer left

    for h in H.keys():
        # if not open continue
        if not hospital_open_indicator[h]: continue

        # if no candidate left continue
        elif len(H[h]) == 0: 
            hospital_open_indicator[h] = 0
            hospital_open_offer_indicator -= 1
            continue
        
        # offer left & candidate on list left
        else:
            # get best remaining candidate and remove from h prefernce list
            best_for_candidate_h = H[h].popleft()
            
            # If a tentative matching already exists with the candidate. Check if h's offer is better than (lower preference number; 1 is better than 3) tentative offer.
            if best_for_candidate_h in T:
                if K[(best_for_candidate_h, h)] < K[(best_for_candidate_h, T[best_for_candidate_h])]:
                    # candidate rejects previous offer, making that hospital open
                    hospital_open_indicator[T[best_for_candidate_h]] = 1

                    # the tentative match with that candidate is updated
                    T[best_for_candidate_h] = h

                    # The current hospital is off the table
                    hospital_open_indicator[h] = 0
                else:
                    # current offer is worse than candidates tentative match. Do nothing. (candidate has already been crossed of the list)
                    continue
            
            # any offer is preferred over None
            else:
                # This assumes every candidate ranks every university, if not, if a candidate does not want a university, you have to check in this place. If they don't want that university, DO NOT create temporary match. Not wanting a university can be indicated as '-1' in the K dictionary above.
                T[best_for_candidate_h] = h

print('\nGale-Shapely algorithm provides the following stable match:')
for candidate, hospital in T.items():
    print(f'{candidate}{" "*(7-len(candidate))}<-> {hospital}')        
    

# You've now seen a couple of important general facts about how the Gale-Shapley algorithm works!

# In any run of the algorithm, these apply:

# 1. Once a candidate has an offer, thereafter they always have an offer.

# 2. Each candidate moves up through their ranking list. The hospital a candidate ends up with when the algorithm terminates is the highest-ranked hospital to make them an offer.

# 3. Hospitals make offers but may repeatedly find themselves with open positions when their chosen candidate accepts a better offer.

# 4. The candidate that a hospital ends up with when the algorithm terminates is the lowest-ranked candidate to whom they made an offer.