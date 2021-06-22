import React, { useState } from 'react';
import ticImage from '../assets/tic.png';
import GameMode from '../components/GameMode';
const GameType = (props) => {
  const [gameType, setGameType] = useState();
  return (
    <>
      {gameType ? (
        <GameMode
          gameType={gameType}
          setGameType={props.setGameType}
          setBoardSize={props.setBoardSize}
          setPlayerSymbol={props.setPlayerSymbol}
        />
      ) : (
        <div data-test="game-container" className="game-container">
          <h3 data-test="game-title" className="game-title">
            Tic Tac Toe
          </h3>
          <div data-test="game-options" className="game-options">
            <img data-test="game-image" src={ticImage} alt="Tic Tac Toe" />
            <div className="options-container">
              <button
                className="action-button"
                data-test="choose-game-type-button"
                onClick={() => {
                  setGameType(1);
                }}
              >
                Play against unbeatable computer
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default GameType;
