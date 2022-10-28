#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Answer #1
# # = 5
# O = 3
# X = 1
# ! = -1
# !! = -3
# !!! = -5


# In[3]:


def check_score(ls):
    score = 0
    for i in ls:
        for j in i:
            if j == '#':
                score += 5
            elif j == 'O':
                score += 3
            elif j == 'X':
                score += 1
            elif j == '!':
                score += -1
            elif j == '!!':
                score += -3
            elif j == '!!!':
                score += -5
            
    if score < 0:
        return 0
    else:
        return score


# In[4]:


# test1

test1 = [['#', '!'], ['!!', 'X']]

check_score(test1)


# In[5]:


# test2

test2 = [['!!!', 'O', '!'], ['X', '#', '!!!'], ['!!', 'X', 'O']]

check_score(test2)


# In[6]:


#Answer 2

def combination(*args):
    result = 1
    for i in args:
        result = result * i
        
    return result


# In[7]:


combination(2,3)


# In[8]:


combination(2,3,4)


# In[9]:


combination(2,3,4,5)


# In[10]:


combination(2,3,4,5,6)


# In[11]:


#Answer 3

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


# In[12]:


def encode_morse(code):
    encode = "" 
    for i in code:
        encode = encode + char_to_dots[i]
        
    return encode


# In[13]:


encode_morse("EDABBIT CHALLENGE")


# In[14]:


encode_morse("HELP ME !")


# In[15]:


# Answer 4

def prime(num):
    
    isPrime = True
    d = 2
    while(d*d <= num):
        if(num%d==0):
            isPrime = False
            break
        d = d + 1

    return isPrime


# In[16]:


prime(7)


# In[17]:


prime(56793)


# In[18]:


# Answer 5

def to_boolean_list(word):
    word_list = []
    word_bool = []
    for i in word:
        word_list.append(ord(i)%2)
        word_bool.append(bool(ord(i)%2))
        
    print(word_list)
    print(word_bool)


# In[19]:


# to_boolean_list("deep") ➞ [False, True, True, False]
to_boolean_list("deep")


# In[20]:


# to_boolean_list("loves") ➞ [False, True, False, True, True]
to_boolean_list("loves")


# In[21]:


# to_boolean_list("tesh") ➞ [False, True, True, False]
to_boolean_list("tesh")


# In[ ]:




