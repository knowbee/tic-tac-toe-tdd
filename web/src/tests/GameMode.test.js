import React from 'react';
import GameMode from '../components/GameMode';
import Enzyme, { shallow } from 'enzyme';
import EnzymeAdapter from '@wojtekmaj/enzyme-adapter-react-17';

Enzyme.configure({
  adapter: new EnzymeAdapter(),
});

/**
 * @function setup
 * @returns {ShallowWrapper}
 */
const setup = () => shallow(<GameMode />);
let wrapper = setup();

const findByTestAttribute = (val) => {
  return wrapper.find(`[data-test='${val}']`);
};
describe('GameMode', () => {
  test('renders  without crashing', () => {
    expect(findByTestAttribute('game-mode-container').length).toBe(1);
  });

  test('shows a title of the game', () => {
    expect(findByTestAttribute('game-title').text()).toBe('Tic Tac Toe');
  });
  test('shows a select input with a message', () => {
    expect(findByTestAttribute('select-text').text()).toBe('Select a symbol and Board size');
  });
  test('shows a button with continue message', () => {
    expect(findByTestAttribute('continue-button').text()).toBe('Continue');
  });
});
