import React from 'react';
import { render } from 'react-dom';
import { Servers } from './components/Servers';
import './css/styles.css';

const App = () => (
  <div>
    <Servers />
  </div>
);

const appDom = document.getElementById('app');
if (appDom) {
  render(<App />, appDom);
}
