# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 13:48:57 2019

@author: Jaspreet
"""

def straight(ranks):
    '''Straight is consecutive 5 different cards.
    So, set(ranks) will see all cards should be different and its length will check they are 5
    And their max difference == 4 will check for consecutive'''
    
    if ranks[0]==14 and ranks[4]==2:
        ranks[0]=1

    if len(set(ranks))== 5 and (max(ranks) - min(ranks)== 4):
        return True
    return False


def flush(suits):
    ''' All of same deck
    So set will make all 5 to 1 and we will check that by its length'''

    if len(set(suits)) == 1:
        return True
    return False 

def kind(n, ranks):
    '''We are getting n which type of kind
    Now take each type of number from ranks and count its presence
    if it matches n then return true else false'''

    '''for r in set(ranks):
        if ranks.count(r) == n:
            return True
    return False'''   

    '''Another implementation
    As we are assuming we are getting ranks in desc order
    eg - [11, 2, 2, 1, 1]'''

    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None        
    

def two_pair(ranks):

    '''
    flag = 0
    for r in set(ranks):
        if ranks.count(r) > 1:
            flag = flag + 1
    if flag == 2:
        return True
    return False
    '''
    hicard = kind(2,ranks)
    locard = kind(2, tuple(reversed(ranks)))  

    if hicard != locard:
        return (hicard, locard)
    return False


def card_ranks(hand):
    ranks=["--23456789TJQKA".index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def card_suits(hand):
    return [s for r,s in hand]

def poker(hands):
    l=[]
    #return max(hands,key=hand_rank)
    for i in range(len(hands)):
        l.append(list(hand_rank(hands[i])))
        
    a= l.index(max(l))
    m=max(l)
    k=['Straight Flush','Four of a Kind','Full House','Flush','Straight','Three of a Kind','Two Pair','One Of a Kind','HighestCard']
    k=list(reversed(k))
    if(m==[8,14]):
        print('Royal Flush')
    else:
        print(k[m[0]])
    return hands[a]
    
    

def hand_rank(hand):
    ranks = card_ranks(hand)
    suits = card_suits(hand)
    
    if straight(ranks) and flush(suits):
        return (8, max(ranks))
    elif kind(4,ranks):
        return (7, kind(4,ranks),kind(1,ranks))
    elif kind(3,ranks) and kind(2,ranks):
        return (6, kind(3,ranks),kind(2,ranks))
    elif flush(suits):
        return (5,)+tuple(ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3,ranks):
        same=kind(3,ranks)
        return (3,same)+tuple([i for i in ranks if i!=same])
    elif two_pair(ranks):
        return (2,)+two_pair(ranks)+(kind(1,ranks))
    elif kind(2,ranks):
        same=kind(2,ranks)
        return (1,same)+tuple([i for i in ranks if i!=same])
    else:
        return (0,)+tuple(ranks)
    


# Uncomment below code and add as many deck you want and find the winner deck
        
"""
print(poker((["AH","2H","3H","4H","5H"],["JS","QS","9S","TS","KS"])))

print(poker((["5C","7C","JC","2C","3C"],["AD","KD","TD","5D","8D"],["QH","QD","QS","QC","6C"],["JH","JS","JC","JD","6C"],["QH","QD","QS","QC","8D"])))

"""




