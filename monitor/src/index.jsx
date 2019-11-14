import React from 'react';
import { render } from 'react-dom';
import App from './App';


const appDom = document.getElementById('app');
if (appDom) {
  render( <App />, appDom);
}
