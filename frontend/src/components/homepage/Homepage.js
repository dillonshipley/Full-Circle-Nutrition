import React, {Component} from 'react';

import { ReactComponent as CalculatorImg} from './calculator.svg';
import { ReactComponent as ToolsImg} from './tools.svg';
import Circle from './images/circle.PNG';

import ReactCurvedText from "react-curved-text";

const circleText = "Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition | Full Circle Nutrition |"

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

  constructor(props){
    super(props);
    this.state = {
      rotation: 220,
      interval: null
    }
  }

  componentDidMount() {
    this.interval = setInterval(() => {
        this.setState({rotation: this.state.rotation - .08} , () => {document.getElementById("circleRotator").style.transform = "rotate(" + this.state.rotation + "deg)"} );
      }, 40);
    }

    componentWillUnmount(){
      clearInterval(this.interval);
    }

    render(){
        return(
        <div id = "mainBodyDiv">


          <div className = "content">
              <div id = "cardHeader">
                take your goals -> make them your habits
              </div>
              <div id = "cardContainer">
                <Card onClick = {(e) => this.props.change("forms", e)} title = "BUILD" text = "from the ground up"/>
                <Card onClick = {(e) => this.props.change("tools", e)} title = "USE" text = "use one of our tools"/>
              </div>
            <div className = "homepageLoginText" onClick = {() => this.changeDisplay("login")}>
                Log in for the complete experience
            </div>
            <div className = "homepageRegisterText">

            </div>
          </div>
          <div className = "background" id = "circleRotator">
            {/*<ReactCurvedText
              width='1620'
              height='1550'
              cx='800'
              cy='759'
              rx={750}
              ry={750}
              startOffset={0}
              reversed={false}
              text={circleText}
              textProps={{"style": {"fontSize":46, "WebkitTextStroke": "2px white"}}}
              textPathProps={{"fill": "#dddddd"}}
              tspanProps={null}
              ellipseProps={null}
              svgProps={null} />*/}
              <img id = "circleText" src = {Circle} alt = "oop" />
          </div>

        </div>
      )
    }
}

export default Homepage;
