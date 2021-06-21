import React, { useEffect, useState } from 'react';
import Grid from './Grid.jsx';
import axios from 'axios';

const Board = ({ playerSymbol, boardSize, gameType }) => {
  const [grids, setGrids] = useState([...Array(boardSize ** 2).keys()]);
  const [winner, setWinner] = useState(null);
  const [tie, setTie] = useState('');

  useEffect(() => {
    console.log(playerSymbol, gameType, boardSize);
  }, []);

  useEffect(() => {});

  const restartGame = () => {
    window.location.reload();
  };
  const handleGridClick = async (move) => {
    if (!winner) {
      grids[move] = playerSymbol;
      const res = await axios.post('https://36a50d7697aa.ngrok.io/play', {
        game_type: parseInt(gameType),
        board_size: parseInt(boardSize),
        first_player: playerSymbol,
        board: grids,
      });
      parseResults(res.data);
    }
  };

  const parseResults = (data) => {
    setGrids(data.board);
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
          {grids.map((grid, i) => (
            <Grid key={i} value={grids[i]} onClick={() => handleGridClick(grid)} data-test={`grid-${i}`} />
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
