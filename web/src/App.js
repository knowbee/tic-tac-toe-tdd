import './App.css';
import GameDisplay from './components/GameDisplay';
import { useState } from 'react';
import GameType from './components/GameType';

function App() {
  const [gameType, setGameType] = useState();
  const [boardSize, setBoardSize] = useState();
  const [playerSymbol, setPlayerSymbol] = useState();

  return (
    <div className="App">
      {gameType && boardSize && playerSymbol ? (
        <GameDisplay boardSize={boardSize} playerSymbol={playerSymbol} gameType={gameType} />
      ) : (
        <GameType setGameType={setGameType} setBoardSize={setBoardSize} setPlayerSymbol={setPlayerSymbol} />
      )}
    </div>
  );
}
export default App;
