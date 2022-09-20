import React, { Component } from 'react';

import FormController from '../FormController';
import Results from '../Results';
import Login from '../Login';
import MacroCalculator from '../tools/MacroCalculator';

//var cardTextOneTitle = "BUILD";
//var cardTextOneDetail = "from the ground up"

//var cardTextOneTitle = "EXPERIMENT";

function Card(props){

  if(props.text === "build"){

  }

  return (
    <div className = "card" id = {"homepageCard" + props.num} onClick = {props.onClick}>
      <div className = "cardIcon">

      </div>
      <div>
        <div className = "cardSpacer"></div>
        <div className = "cardInfoText">{props.text}</div>
      </div>
    </div>

  );
}

class Body extends Component{
    constructor(props){
      super(props);
      this.state = {
        display: "start"
      }
    }


    render(){
      if(this.state.display === "forms"){
        return (
          <div>
            <FormController back = {() => this.setState({display: "start"})} />
          </div>
        )
      } else if (this.state.display === "start"){
        return (
            <div id = "mainBodyDiv">
                <div id = "homePageTitle">Goal to Table Nutrition </div>
                <div id = "homePageCardContainer">
                    <Card onClick = {() => this.setState({display: "forms"})} text = "Build From the Ground Up"/>
                    <Card onClick = {() => this.setState({display: "tools"})} text = "Use One of Our Tools"/>
                </div>
                <div className = "homepageLoginText" onClick = {() => this.setState({display: "login"})}>
                    Log in for the complete experience
                </div>
                <div className = "homepageRegisterText">

                </div>
            </div>
        );
      } else if (this.state.display === "results"){
          <Results />
      } else if (this.state.display === "tools"){
          <MacroCalculator />
      }else if (this.state.display === "login"){
        return(
          <div>
            <Login back = {() => this.setState({display: "start"})}/>
          </div>
        );
      }
    }
}

export default Body;
