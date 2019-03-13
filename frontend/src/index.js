import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/react-bootstrap-table/dist/react-bootstrap-table-all.min.css';
import Main from './Main';
import * as serviceWorker from './serviceWorker';
//document.body.style = 'background: black;';
ReactDOM.render(<Main />, document.getElementById('root'));

// If you want your app to work offline and load  s faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
