import React from 'react';

const Grid = (props) => {
  return (
    <button className="board__grid" onClick={props.onClick} data-test="grid">
      {props.value}
    </button>
  );
};

export default Grid;
