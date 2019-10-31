import React from 'react';
import { render } from 'react-dom'

const App = () => <div>React Live</div>;

const appDom = document.getElementById('app');
if (appDom) {
    render(<App/>, appDom);
}
