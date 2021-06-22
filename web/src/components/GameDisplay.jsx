import React, { useEffect, useState } from 'react';
import Cell from './Cell.jsx';
import axios from 'axios';

const Board = ({ playerSymbol, boardSize, gameType }) => {
  const [cells, setCells] = useState([...Array(boardSize ** 2).keys()]);
  const [winner, setWinner] = useState(null);
  const [tie, setTie] = useState('');

  useEffect(() => {
    console.log(playerSymbol, gameType, boardSize);
  }, []);

  useEffect(() => {});

  const restartGame = () => {
    window.location.reload();
  };
  const handleCellClick = async (move) => {
    if (!winner) {
      cells[move] = playerSymbol;
      const res = await axios.post('https://36a50d7697aa.ngrok.io/play', {
        game_type: parseInt(gameType),
        board_size: parseInt(boardSize),
        first_player: playerSymbol,
        board: cells,
      });
      parseResults(res.data);
    }
  };

  const parseResults = (data) => {
    setCells(data.board);
    if (data.finished) {
      setWinner(data.winner);

      if (data.winner == null) {
        setTie('Tie');
      }
    }
  };
  return (
    <div className="board-container" data-test="board-container">
      <h3 data-test="game-title" className="game-title">
        Tic Tac Toe
      </h3>

      <div className="board">
        {winner && (
          <h2>
            Winner is<span className="__winner">{winner}</span>{' '}
          </h2>
        )}
        {tie && (
          <h2 className="board-heading">
            The Game is a <span className="__tie">{tie}</span>{' '}
          </h2>
        )}
        <div className="board-row">
          {cells.map((cell, i) => (
            <Cell key={i} value={cells[i]} onClick={() => handleCellClick(cell)} data-test={`cell-${i}`} />
          ))}
        </div>

        <button className="action-button" data-test="choose-game-type-button" onClick={() => restartGame()}>
          Restart the game
        </button>
      </div>
    </div>
  );
};

export default Board;
