
# coding: utf-8

# In[1]:


def long_sub_palim(string):
    string_list = [x for x in string]
    #print string_list
    
    palindromes = []
    
    #case aa
    case_aa_ind = []
    prev = string_list[0]
    for i in range(1, len(string_list)):
        curr = string_list[i]
        if curr == prev:
            case_aa_ind.append(i)
        prev = curr
    #print case_aa_ind
    
    for i in case_aa_ind:
        poss_len = min(i,len(string_list)-i)
        
        for j in range(poss_len):
            #print poss_len
            #print i, j
            if (i+j == len(string_list)-1) and (string_list[i-j-1] == string_list[i+j]):
                #print i+j
                #print string_list[i-j-1]
                #print string_list[i+j]
                palindrome = ''.join(string_list[(i-j-1):])
                palindromes.append(palindrome)
            
            if string_list[i-j-1] != string_list[i+j]:
                palindrome = ''.join(string_list[(i-j):(i+j)])
                palindromes.append(palindrome)
                break
            
            
    
    #case aba
    case_aba_ind = []
    prev = string_list[0]
    
    for i in range(1, len(string_list)-1):
        curr = string_list[i+1]
        if curr == prev:
            case_aba_ind.append(i)
        prev = string_list[i]
    
    #print case_aba_ind
    
    for i in case_aba_ind:
        poss_len = min(i,(len(string_list)-i-1))
        for j in range(poss_len):
            #print poss_len
            #print i, j
            if (i+j == len(string_list)-2) and (string_list[i-j-1] == string_list[i+j+1]):
                #print i+j
                #print string_list[i-j-1]
                #print string_list[i+j]
                palindrome = ''.join(string_list[(i-j-1):])
                palindromes.append(palindrome)
            
            if string_list[i-j-1] != string_list[i+j+1]:
                palindrome = ''.join(string_list[(i-j):(i+j+1)])
                palindromes.append(palindrome)
                break
    
    if len(palindromes) == 0:
        return None
    longest = palindromes[0]
    for i in palindromes:
        if len(i)>len(longest):
            longest = i
    
    return longest


# In[2]:


print long_sub_palim('asdllsacattacasllasadsda')
print long_sub_palim('qweqwabcjejejejcbaasdas')
#print len('asdsabctcba')
print long_sub_palim('asdsabccba')
print long_sub_palim('asdsabctcba')
print long_sub_palim('abccba')
print long_sub_palim('abctcba')

