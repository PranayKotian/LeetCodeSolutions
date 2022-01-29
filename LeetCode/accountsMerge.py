#https://leetcode.com/problems/accounts-merge/
#Title: 721. Accounts Merge
#Difficulty: Medium
#Language: Python
#Author: Pranay Kotian

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else: #rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            
        par = {}
        rank = {}
        emailtoname = {}
        
        #adds all emails to parent dict
        #initializes all email ranks to 1
        #adds all email name pairs to emailtoname conversion dictionary
        
        for acct in accounts:
            name = acct[0]
            for email in acct[1:]:
                par[email] = email
                rank[email] = 1
                emailtoname[email] = name
        
        #unions all emails that are connected to the same person
        
        for acct in accounts:
            email1 = acct[1]
            for email in acct[2:]:
                union(email1, email)
        
        #appends all emails that are connected (have the same parent) to the same list
        
        groups = defaultdict(list) 
        for email in par:
            r = find(email)
            groups[r].append(email)
        
        #connects name to each list using emailtoname dict and outputs total list
        
        out = []
        for key in groups:
            out.append([emailtoname[key]] + sorted(groups[key]))
        return out