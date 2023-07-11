'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    follows = False
    followed_by = False

    # print(social_graph[from_member]['following'])

    for member in (social_graph[from_member]['following']) :
        if member == to_member :
            follows = True
            break
        else :
            follows = False
    
    for member in (social_graph[to_member]['following']) :
        if member == from_member :
            followed_by = True
            break
        else :
            followed_by = False
        
    
    if follows and followed_by :
        return "friends"
    
    elif follows :
         return "follower"

    elif followed_by :
         return "followed by"

    else :
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = (len(board))
    characters = []
    winner = None

    for i in board:
        for j in i:
            characters.append(j)
    unique_characters = list(set(characters))
    #return(unique_characters)

    # check row
    for i in board :
        if len(set(i)) == 1 :
            winner = i[0]
            break

    # check column
    column_count = 0
    columns = []
    while column_count <= size - 1 :
        for i in board:
            columns.append(i[column_count])
        column_count += 1
    #return(columns)

    # dividing column into columns
    column_list = []
    for i in range(0,len(columns),size):
        column_list.append(columns[i:i+size])
    
    for i in column_list :
            if len(set(i)) == 1 :
                winner = i[0]
                break


    # check diagonal
    diagonals = []
    left_diagonal = []
    right_diagonal = []
    
    ld_count = 0
    for i in board:
        left_diagonal.append(i[ld_count])
        ld_count += 1
    diagonals.append(left_diagonal)

    rd_count = size - 1
    for i in board:
        right_diagonal.append(i[rd_count])
        rd_count -= 1
    diagonals.append(right_diagonal)

    for i in diagonals :
            if len(set(i)) == 1 :
                winner = i[0]
                break

    if winner == None :
        return "NO WINNER"
    else :
        return winner


legs1 = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}


def eta(first_stop, second_stop, route_map):

    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    import itertools
    try:
        return(route_map[first_stop, second_stop]["travel_time_mins"])
    except:
        
        routes = {}
        travel_time = []

        #return(dict)

        for route in route_map :
            if route[0] == first_stop :
                first_index = list(route_map).index(route)
                #return first_index

        for route in route_map :
            if route[1] == second_stop :
                second_index = list(route_map).index(route)
                #return second_index
        
        routes = dict(itertools.islice(route_map.items(), first_index ,second_index+1))


        tempList = list(dict.keys(route_map))
        #print(tempList)
        
        #endKey = tempList[second_index]

        sumTime = 0
        while (first_index % len(tempList) != second_index):
            startKey = tempList[first_index % len(tempList)]
            sumTime += route_map[startKey]["travel_time_mins"]
            first_index += 1

        if(first_index >= len(tempList)):
            sumTime += route_map[tempList[first_index % len(tempList)]]["travel_time_mins"]
        else:
            sumTime += route_map[tempList[first_index]]["travel_time_mins"]
        
        print(first_index)
        print(second_index)
        #for route in routes.values() :
        #    travel_time.append((route['travel_time_mins']))
            
    #return(sum(travel_time))
    return(sumTime)
