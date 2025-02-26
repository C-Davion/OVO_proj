# %% #exported from a Jupyter Notebook
import numpy as np

sub_s = "₀₁₂₃₄₅₆₇₈₉"

# %% [markdown]
# Create matrix $\Pi$

# %%
def create_pi(C: np.ndarray):
    pi=np.argsort(C,axis=0)
    return pi

# %% [markdown]
# Create matrix $\Delta C$

# %%
def create_delta(C:np.ndarray,pi:np.ndarray):
    sortedC=np.take_along_axis(C,pi,axis=0)
    sortedC=np.vstack((np.zeros((1,C.shape[1])),sortedC))
    deltaC=np.diff(sortedC,axis=0)
    return deltaC



# %%
def create_term_dictionnary(pi:np.ndarray,deltaC:np.ndarray):
    '''
    No the most efficient implementation, but the most intuitive
    due to small size of image patches, the for loops doesn't take much time
    '''
    terms={}
    terms[tuple([0])]=np.sum(deltaC[0,:]) #constant term
    for i in range(pi.shape[0]-1):
        for j in range(pi.shape[1]):
            key=tuple(sorted([pi[row][j]+1 for row in range(i+1)]))
            if key in terms:
                terms[key]+=deltaC[i+1][j]
            else:
                terms[key]=deltaC[i+1][j]
    return terms


def print_polynomials(terms:dict):
    def makestring(sub_index:list):
        temp=''
        for x in sub_index:
            temp+='y'+'y.'.join(sub_s[x])
        return temp
    out=""
    for _,key in enumerate(terms):
        val=terms[key]
        key=list(key)#change to list to iterate through
        out+=f'+{val}'+makestring(key)
    #print(out[1:])
    return None


def driver(C:np.ndarray): #driver functions
    pi=create_pi(C)
    deltaC=create_delta(C,pi)
    terms=create_term_dictionnary(pi,deltaC)
    clean_terms= {k: int(v) for k, v in terms.items() if v != 0.0} # removes the monomes with coefficient 0 and swtiched the format to int
    deg=max((len(key) for key,value in clean_terms.items()),default=0)
    #print("Returned from driver:", clean_terms, deg)
    return clean_terms,deg




#==========================TESTIN+++++++++++++++++++++++++++++++++++++++++
paperexample=np.array([[8,8,8,5],
                        [12,7,5,7],
                        [18,2,3,1],
                        [5,18,9,8]])
# #paperexample=np.array([[7,7,7],
#                        [4,4,4],
#                        [3,3,3]])
pi=create_pi(paperexample)


deltaC=create_delta(paperexample,pi)
poly,deg=driver(paperexample)
#print_polynomials(poly)

#print_polynomials(terms) #uncomment this line to display the polynomials.




