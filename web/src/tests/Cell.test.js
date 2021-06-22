import React from 'react';
import Cell from '../components/Cell';
import Enzyme, { shallow } from 'enzyme';
import EnzymeAdapter from '@wojtekmaj/enzyme-adapter-react-17';

Enzyme.configure({
  adapter: new EnzymeAdapter(),
});

/**
 * @function setup
 * @returns {ShallowWrapper}
 */
const setup = () => shallow(<Cell />);
let wrapper = setup();

const findByTestAttribute = (val) => {
  return wrapper.find(`[data-test='${val}']`);
};
describe('Cell', () => {
  test('renders  without crashing', () => {
    expect(findByTestAttribute('cell').length).toBe(1);
  });

  test('has content', () => {
    expect(findByTestAttribute('cell').text()).toBe('');
  });
});
