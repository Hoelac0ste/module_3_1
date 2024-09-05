
calls = 0
list_to_search = ['This evening I do my homework', 'Guitar', 'Piano']
string = "I Do MY Homework"

def count_calls():
    global calls
    calls += 1


def string_info(string):
    string = (len(string), string.upper(), string.lower())
    print(string)
    count_calls()
    
def is_contains(string, list_to_search):
    
    for i in range(len(list_to_search)):
        string = string.lower()
        list_to_search[i] = str(list_to_search[i].lower())
        if string in list_to_search[i]:
            print('True')
        else:
            continue
    count_calls()

    
string_info('Pink Floyd')
string_info('Metallica')
is_contains(string, list_to_search)
print(calls)