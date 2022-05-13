#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import math
import statistics


# In[2]:


data_dir1 = r'C:\Users\Dan\(2) privacy\part1\\'
file1 = 'seed_G1.edgelist'

data_dir2 = r'C:\Users\Dan\(2) privacy\part1\\'
file2 = 'seed_G2.edgelist'

data_dir3 = r'C:\Users\Dan\(2) privacy\part1\\'
file3 = 'seed_node_pairs.txt'


# In[3]:


G1 = nx.read_edgelist(data_dir1+file1, create_using=nx.Graph(), nodetype=int)
G2 = nx.read_edgelist(data_dir2+file2, create_using=nx.Graph(), nodetype=int)

print(nx.info(G1))
print("")
print(nx.info(G2))

arrayG1 = list(nx.nodes(G1))
arrayG2 = list(nx.nodes(G2))

seedPairG1 = []
seedPairG2 = []

with open(data_dir3+file3, "r") as text_file:
    for line in text_file:
        line = line.strip()
        number1 , number2 = line.split(" ")
        seedPairG1.append(int(number1))
        seedPairG2.append(int(number2))


# In[4]:


nonMatchedG1 = [x for x in arrayG1 if (x not in seedPairG1)]
nonMatchedG1.sort()
nonMatchedG2 = [x for x in arrayG2 if (x not in seedPairG2)]

threshold = 2.66

for x in nonMatchedG1:
    scoreList = []
    degreeOfV = len(list(nx.neighbors(G1, x)))
    for y in nonMatchedG2:
        count1 = 0
        count2 = 0
        matchedIndex1 = []
        matchedIndex2 = []
        degreeOfU = len(list(nx.neighbors(G2, y)))
        neighbors1 = list(nx.neighbors(G1, x))
        neighbors2 = list(nx.neighbors(G2, y))
        for nodeV in neighbors1:
            count1 = 0
            for a in seedPairG1:
                if nodeV == a:
                    matchedIndex1.append(count1)
                    break
                count1 = count1 + 1
        for nodeU in neighbors2:
            count1 = 0
            for b in seedPairG2:
                if nodeU == b:
                    matchedIndex2.append(count1)
                    break
                count1 = count1 + 1
        for node1 in matchedIndex1:
            for node2 in matchedIndex2:
                if node1 == node2:
                    count2 = count2 + 1
        scores = (count2)/(math.sqrt(degreeOfV) * math.sqrt(degreeOfU))
        scoreList.append(scores)
    std = statistics.pstdev(scoreList)
    if std != 0.0:
        temp_max = max(scoreList)
        test = zip(scoreList, nonMatchedG2)
        test = list(test)
        for z in test:
            temp_pos = z[0]
            if temp_max == temp_pos:
                node_pos = z[1]
                break
        print("Node V =", x)
        max1 = max(scoreList)
        scoreList.remove(max1)
        max2 = max(scoreList)
        ecce = (max1 - max2)/(std)
        print("Std =", std)
        print("Max1 =", max1)
        print("Max2 =", max2)
        print("ECCE = (", max1, "-", max2, ") /", std, "=", ecce)
        print("ECCE =", ecce)
        if ecce > threshold:
            seedPairG1.append(x)
            seedPairG2.append(node_pos)
            nonMatchedG2.remove(node_pos)
        print(" ")
        print("-----")
        print(" ")


# In[5]:


print(list(zip(seedPairG1, seedPairG2)))


# In[7]:


seedPairsOutput1 = list(zip(seedPairG1, seedPairG2))

with open(r"C:\Users\Dan\(2) privacy\project1outputfirstpass.txt", "w") as txt_file:
    for line in seedPairsOutput1:
        txt_file.write(" ".join([str(n) for n in line]) + "\n")


# In[9]:


#seedPairsOutput1 = list(zip(seedPairG1, seedPairG2))

#with open(r"C:\Users\Dan\(2) privacy\project1outputsecondpass.txt", "w") as txt_file:
#    for line in seedPairsOutput1:
#        txt_file.write(" ".join([str(n) for n in line]) + "\n")
#second pass just to show


# In[ ]:




