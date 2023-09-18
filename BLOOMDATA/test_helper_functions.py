import pytest
# from sprint_9_project import helper_functions as hf
import sprint_9_project.helper_functions as hf
list1 = [1,2,3]
list2 = [4,5,6]
adjectives = ["blue","large","grainy","substantial","potent","thermonuclear"]
nouns = ["food","house","tree","bicycle","toupee","phone"]
def test_words_rand():
    assert isinstance(hf.words_rand(list1,list2),str) 
    assert isinstance(hf.words_rand(adjectives,nouns),str)
    