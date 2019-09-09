message = raw_input('Enter your message: ')
letter = list(message)

#print letter

def lists_number(number):
    result = []
    for l in number:
        result.append(ord(l))
    return result

#print lists_number(letter)


N = input('please enter the Public Key number: ')
e = input('please enter the Private Key number: ') 

def cypher_lists_number(cypher_number):
    outcome = []
    for c in cypher_number:
        outcome.append((c ** e) % N)
    return outcome

remainder_2 = cypher_lists_number(lists_number(letter))

def to_string(string):
    outcome_1 = []
    for n in string:
        outcome_1.append(str(n))
    return outcome_1

remainder_1 = to_string(remainder_2)

remainder_1 = ' '.join(remainder_1)
print remainder_1


