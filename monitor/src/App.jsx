import React from 'react';
import { Servers } from './components/Servers';
import { UserList } from './components/UserList';
import { Navbar } from './components/Navbar';
import './css/styles.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
  useHistory,
  useLocation
} from "react-router-dom";


export default function App () {
  return (
    <div className="wrapper">
      <div className="main-panel">
        <Navbar />
        <div className="content">
          <Router>
            <div>
              <Switch>
                <Route exact path="/">
                  <Servers />
                </Route>
                <Route exact path="/users">
                  <UserList />
                </Route>
              </Switch>
            </div>
          </Router>
        </div>
      </div>
    </div>
  )
};
