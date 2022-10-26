import React, { Component } from 'react';

import FormController from '../FormController';
import Results from '../Results';
import Login from '../Login';
import Tools from '../tools/Tools';

import { ReactComponent as CalculatorImg} from './calculator.svg';
import { ReactComponent as ToolsImg} from './tools.svg';

//var cardTextOneTitle = "BUILD";
//var cardTextOneDetail = "from the ground up"

//var cardTextOneTitle = "EXPERIMENT";

function Card(props){
  let mysrc;
  if(props.title === "BUILD")
    mysrc = <CalculatorImg className ="homepageIcon"/>;
  else
    mysrc = <ToolsImg className ="homepageIcon"/>;

  return (
    <div className = "card homepageCard" id = {"homepageCard" + props.num} onClick = {props.onClick}>
      <div className = "cardIcon">
        {mysrc}
      </div>
      <div>
        <div className = "cardSpacer"></div>
        <div className = "cardTitle">{props.title}</div>
        <div className = "cardInfoText">{props.text}</div>
      </div>
    </div>
  );
}

class Body extends Component{
    constructor(props){
      super(props);
      this.state = JSON.parse(localStorage.getItem('navState')) || {
          display: "start"
      }
    }

    changeDisplay(display){
      console.log("display: " + display);
      this.setState({display: display}, () => {
        localStorage.setItem('navState', JSON.stringify(this.state));
      });
    }

    reset(){
      localStorage.clear();
    }

    render(){
      if(this.state.display === "forms"){
        return (
          <div>
            <FormController back = {() => this.changeDisplay("start")} />
          </div>
        )
      } else if (this.state.display === "start"){
        return (
            <div id = "mainBodyDiv">
                <div id = "homePageTitle">Goal to Table Nutrition </div>
                <div id = "homePageCardContainer">
                    <Card onClick = {(e) => this.changeDisplay("forms", e)} title = "BUILD" text = "from the ground up"/>
                    <Card onClick = {(e) => this.changeDisplay("tools", e)} title = "USE" text = "use one of our tools"/>
                </div>
                <div className = "homepageLoginText" onClick = {() => this.changeDisplay("login")}>
                    Log in for the complete experience
                </div>
                <button onClick = {() => this.reset()}>Reset</button>
                <div className = "homepageRegisterText">

                </div>
            </div>
        );
      } else if (this.state.display === "results"){
          <Results />
      }else if (this.state.display === "login"){
        return(
          <Login back = {() =>this.changeDisplay("start")}/>
        );
      } else if (this.state.display === "tools"){
        return(
            <Tools back = {() =>this.changeDisplay("start")}/>
        );
      }
    }
}

export default Body;
