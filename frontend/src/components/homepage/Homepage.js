import React, {Component} from 'react';

import { ReactComponent as CalculatorImg} from './calculator.svg';
import { ReactComponent as ToolsImg} from './tools.svg';

import ReactCurvedText from "react-curved-text";

const circleText = "Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition"

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

class Homepage extends Component {

    render(){
        return(
        <div id = "mainBodyDiv">
            <div id = "homePageTitle">Full Circle Nutrition </div>
            <ReactCurvedText width='1080'
              height='1000'
              cx='590'
              cy='377'
              rx={500}
              ry={500}
              startOffset={0}
              reversed={false}
              text={circleText}
              textProps={{"style": {"fontSize":74}}}
              textPathProps={{"fill": "#ffd6d6"}}
              tspanProps={null}
              ellipseProps={null}
              svgProps={null} />
            <div id = "homePageCardContainer">
              <div id = "homepageCircleText">
                <Card onClick = {(e) => this.props.change("forms", e)} title = "BUILD" text = "from the ground up"/>
                <Card onClick = {(e) => this.props.change("tools", e)} title = "USE" text = "use one of our tools"/>
              </div>
            </div>
            <div className = "homepageLoginText" onClick = {() => this.changeDisplay("login")}>
                Log in for the complete experience
            </div>
            <div className = "homepageRegisterText">

            </div>
        </div>
        );
    }
}

export default Homepage;
