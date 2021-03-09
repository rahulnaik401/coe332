#!/usr/bin/env python3
import json
import random
import sys

def breed(parent1, parent2):
	kid={}
	kid['head']=random.choice([parent1['head'],parent2['head']])
	kid['body']=random.choice([parent1['body'],parent2['body']])
	kid['arms']=random.choice([parent1['arms'],parent2['arms']])
	kid['legs']=random.choice([parent1['legs'],parent2['legs']])
	kid['tail']=random.choice([parent1['tail'],parent2['tail']])
	
	assert (isinstance(parent1, dict) and  isinstance(parent2,dict))
	return kid
def main():

    with open(sys.argv[1], 'r') as f:
        animal_dict = json.load(f)
    
    parent1=random.choice(animal_dict['animals'])
    parent2=random.choice(animal_dict['animals'])
    kid=breed(parent1,parent2)
    #print(random.choice(animal_dict['animals'])
    print('Parents:')
    print(parent1)
    print(parent2)
    print('Kid:')
    print(kid)     

if __name__ == '__main__':
    main()
