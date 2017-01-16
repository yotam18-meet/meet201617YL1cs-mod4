from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, measure):
        super(Square, self).__init__(measure, measure)
    def set_height(self, new_measure):
        super(Square, self).set_height(new_measure)
        super(Square, self).set_length(new_measure)
    def set_length(self, new_measure):
        super(Square, self).set_length(new_measure)
        super(Square, self).set_height(new_measure)
            
                
    
