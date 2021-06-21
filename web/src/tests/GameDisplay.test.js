import React from 'react';
import GameDisplay from '../components/GameDisplay';
import Enzyme, { shallow } from 'enzyme';
import EnzymeAdapter from '@wojtekmaj/enzyme-adapter-react-17';

Enzyme.configure({
  adapter: new EnzymeAdapter(),
});

/**
 * @function setup
 * @returns {ShallowWrapper}
 */
const setup = () => shallow(<GameDisplay boardSize={3} />);
let wrapper = setup();

const findByTestAttribute = (val) => {
  return wrapper.find(`[data-test='${val}']`);
};
describe('GameDisplay', () => {
  test('renders without crashing', () => {
    expect(findByTestAttribute('board-container').length).toBe(1);
  });

  test('renders cells', () => {
    for (let index = 0; index < 9; index++) {
      expect(findByTestAttribute(`cell-${index}`).length).toBe(1);
    }
  });
});
