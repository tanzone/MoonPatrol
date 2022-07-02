'''
Interface to be implemented by each game character
'''
class Actor():
    '''
    Called by Arena, at the actor's turn
    '''
    def move(self):                             raise NotImplementedError('Abstract method')

    '''
    Called by Arena, whenever the `self` actor collides with some
    `other` actor
    '''
    def collide(self, other: 'Actor'):          raise NotImplementedError('Abstract method')

    '''
    Return the rectangle containing the actor, as a 4-tuple of ints:
    (left, top, width, height)
    '''
    def position(self) -> (int, int, int, int): raise NotImplementedError('Abstract method')

    '''
    Return the position (x, y, w, h) of current sprite, if it is contained in
    a larger image, with other sprites. Otherwise, simply return (0, 0, 0, 0)
    '''
    def symbol(self) -> (int, int, int, int):   raise NotImplementedError('Abstract method')
