import React, {Component} from 'react';

import { ReactComponent as CalculatorImg} from './calculator.svg';
import { ReactComponent as ToolsImg} from './tools.svg';

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
        this.setState({rotation: this.state.rotation + 1});
        console.log(this.state.rotation);
      }, 20);
    }

    componentWillUnmount(){
      clearInterval(this.interval);
    }

    render(){
      const style = {transform: "rotate(" + this.state.rotation + ")deg"}
        return(
        <div id = "mainBodyDiv">

          <div id = "circleRotator" style={style}>
            <ReactCurvedText width='1920'
              height='1000'
              cx='875'
              cy='459'
              rx={750}
              ry={750}
              startOffset={0}
              reversed={false}
              text={circleText}
              textProps={{"style": {"fontSize":46, "-webkit-text-stroke": "2px white"}}}
              textPathProps={{"fill": "#000000"}}
              tspanProps={null}
              ellipseProps={null}
              svgProps={null} />
          </div>
              <div id = "homepageCircleText">
                <Card onClick = {(e) => this.props.change("forms", e)} title = "BUILD" text = "from the ground up"/>
                <Card onClick = {(e) => this.props.change("tools", e)} title = "USE" text = "use one of our tools"/>
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
