import React from 'react';

const Cell = (props) => {
  return (
    <button className="board__cell" onClick={props.onClick} data-test="cell">
      {props.value}
    </button>
  );
};

export default Cell;
