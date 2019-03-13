import React, { Component } from "react";
import {Card} from "react-bootstrap";
import {
  Route,
  HashRouter
} from "react-router-dom";

import Home from "./Home";
import AddPrices from "./AddPrices";
import Contact from "./Contact";
import Potatoes from "./Potatoes";
import Clients from "./Clients";
import Login from "./Login";
import NavigationBar from "./NavigationBar";

class Main extends Component {
  render() {

    var letterStyle = {
      fontSize: 14,
    };

    return (
        <HashRouter>
        <div style={letterStyle}>
            <NavigationBar />
                <Route exact path="/" component={Home}/>
                <Route exact path="/AddPrices" component={AddPrices}/>
                <Route exact path="/clients" component={Clients}/>
                <Route exact path="/contact" component={Contact}/>
                <Route exact path="/potatoes" component={Potatoes}/>
                <Route exact path="/login" component={Login}/>
        </div>
        </HashRouter>
        )
    }
}
export default Main;
