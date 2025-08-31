from db import get_counter_date


def calculate_count(db, counter):
    ''' calculate the count of the count.

    print db: instulized sqlite3 databased connection
    print counter: name of the counter present in the db
    return: lenght of the counter increment event
    '''
    date= get_counter_date(db, counter)
    return len(date)