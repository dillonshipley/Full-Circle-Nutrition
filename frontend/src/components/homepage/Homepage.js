import React, {Component} from 'react';

class Homepage extends Component {
    constructor(props){
        super(props);

    }

    render(){
        return(
        <div id = "mainBodyDiv">
            <div id = "homePageTitle">Full Circle Nutrition </div>
            <div id = "homePageCardContainer">
              <div id = "homepageCircleText">
                <Card onClick = {(e) => this.changeDisplay("forms", e)} title = "BUILD" text = "from the ground up"/>
                <Card onClick = {(e) => this.changeDisplay("tools", e)} title = "USE" text = "use one of our tools"/>
              </div>
            </div>
            <div className = "homepageLoginText" onClick = {() => this.changeDisplay("login")}>
                Log in for the complete experience
            </div>
            <button onClick = {() => this.reset()}>Reset</button>
            <div className = "homepageRegisterText">

            </div>
        </div>
        );
    }
}