"""
ui class is responsible for getting data from the user, validating data, and displaying data
"""
def get_string(message):
    while True:
        response = input(message)
        if response is not None:
            return response

def get_int(message):
    while True:
        try:
            response = int(input(message))
            return response
        except ValueError:
            print('Please enter a number ')


def get_int_in_range(message, min, max):
    while True:
        response = get_int(message)
        if response in range (min, max + 1):
            return response
        else:
            print(f'Please enter a valid number between {min} & {max}')
        
def program_intro_message():
    print('\n WELCOME TO ~ARTIST OBSESSED~ \n')
    print('The program will search for information about an artist and provide their follower count, album artwork and song lyrics.')
    print('You also can bookmark searches and search from your previously bookmarked searches.')
    print('please select an option below to begin: \n')

def save_bookmark():
    save_bookmark = input('Do you want to save this as a bookmark? (Y/N): ')
    
    if save_bookmark == 'Y' or save_bookmark == 'y':
        return True
    elif save_bookmark == 'N' or save_bookmark == 'n': 
        return False
    else:
        print('Please enter a valid Y/N entry.')

def search_by_id():
    message = 'Please enter the ID of the Bookmark you would like to select: '
    id = get_int(message)
    return id

def print_message(msg):
    return print(msg)

