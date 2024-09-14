def magic_calculation(a, b):
    ''' 
    Import the add and sub functions from the module magic_calculation_102
    '''
    from magic_calculation_102 import add, sub

    ''' 
    Compare a and b: if a is less than b, use add function 
    '''
    if a < b:
        ''' Add a and b and store the result in c '''
        c = add(a, b)

        ''' 
        Loop through the range from 4 to 6, and add each i to c 
        using the add function 
        '''
        for i in range(4, 6):
            c = add(c, i)

        ''' Return the final value of c '''
        return c
    else:
        ''' 
        If a is greater than or equal to b, return the result of sub(a, b) 
        '''
        return sub(a, b)
