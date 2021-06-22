import React, { useState } from 'react';

const GameMode = (props) => {
  const [symbol, setSymbol] = useState('X');
  const [size, setSize] = useState(3);

  const handleChange = (e) => {
    setSymbol(e.target.value);
  };
  const handleSizeChange = (e) => {
    setSize(e.target.value);
    console.log(size);
  };

  const startGame = () => {
    props.setPlayerSymbol(symbol);
    props.setGameType(props.gameType);
    props.setBoardSize(size);
  };
  return (
    <div className="game-container" data-test="game-mode-container">
      <h3 data-test="game-title" className="game-title">
        Tic Tac Toe
      </h3>
      <h3 data-test="select-text">Select a symbol and Board size</h3>
      <div className="select-container">
        <form>
          <select onChange={handleChange} className="custom-select">
            <option value="X">X</option>
            <option value="O">O</option>
          </select>
        </form>
        <form>
          <select onChange={handleSizeChange} className="custom-select">
            <option value="3">3 x 3</option>
          </select>
        </form>
      </div>
      <button className="action-button" data-test="continue-button" onClick={() => startGame()}>
        Continue
      </button>
    </div>
  );
};

export default GameMode;
