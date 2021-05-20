class HandleTurns:

  def __init__(self):
      self.currentPlayerSymbol = None

  def change(self):
      if( self.currentPlayerSymbol == 'X' ):
          self.set_currentPlayerSymbol('O')
      else:
          self.set_currentPlayerSymbol('X')

  def set_currentPlayerSymbol(self, symbol):
      self.currentPlayerSymbol = symbol
