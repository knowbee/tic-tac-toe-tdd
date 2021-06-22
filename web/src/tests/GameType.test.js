import React from 'react';
import GameType from '../components/GameType';
import Enzyme, { shallow } from 'enzyme';
import EnzymeAdapter from '@wojtekmaj/enzyme-adapter-react-17';

Enzyme.configure({
  adapter: new EnzymeAdapter(),
});

/**
 * @function setup
 * @returns {ShallowWrapper}
 */
const setup = () => shallow(<GameType />);
let wrapper = setup();

const findByTestAttribute = (val) => {
  return wrapper.find(`[data-test='${val}']`);
};
describe('GameType', () => {
  test('renders  without crashing', () => {
    expect(findByTestAttribute('game-container').length).toBe(1);
  });

  test('shows a title of the game', () => {
    expect(findByTestAttribute('game-title').text()).toBe('Tic Tac Toe');
  });
  test('shows a list of game type options', () => {
    expect(findByTestAttribute('game-options').length).toBe(1);
  });
  test('shows a preview image of the game', () => {
    expect(findByTestAttribute('game-image').length).toBe(1);
  });
  test('shows an option of playing against unbeatable computer', () => {
    expect(findByTestAttribute('choose-game-type-button').length).toBe(1);
  });
  test('shows a message saying to play against unbeatable computer', () => {
    expect(findByTestAttribute('choose-game-type-button').text()).toBe('Play against unbeatable computer');
  });
});
