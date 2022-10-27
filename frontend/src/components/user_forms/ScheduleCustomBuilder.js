import React, {Component, useState} from 'react';

function Counter(props){
  

  
  return (
    <div className = "counterContainer">
      <div className = "counterDiv counterDivSymbol">-</div>
      <div className = "counterDiv">{props.num}</div>
      <div className = "counterDiv counterDivSymbol">+</div>
    </div>
  );
}

class DaySelectorBlock extends React.Component{
  
  constructor(props){
    super(props);
    this.state = {
      MPD: 3,
      breakfast: false,
      SPD: 1
    }
  }

  increase(props){
    if(props.type === "MPD")
      this.setState({MPD: this.state.MPD + 1});
    else if (props.type === "SPD")
      this.setState({MPD: this.state.MPD + 1});
  }

  decrease(props){
    if(props.type === "MPD")
      this.setState({MPD: this.state.MPD - 1});
    else if (props.type === "SPD")
      this.setState({MPD: this.state.MPD - 1});
  }

  render(){
    return (
      <div id = "daySelectorCB">
        <p className = "dayLabel">{this.props.day}</p>
        <Counter num = {this.state.MPD} down = {(e) => this.decrease(e)} up = {(e) => this.increase(e)} />
        <Counter num = {this.state.SPD} down = {(e) => this.decrease(e)} up = {(e) => this.increase(e)} />
      </div> 
    )
  }
}

export default class ScheduleCustomBuilder extends Component {
  constructor(props){
    super(props);
  }

  componentDidMount(){
    console.log("sup");
  }

  render(){
      return (
        <div>
          <DaySelectorBlock day = "Sunday" />
          <DaySelectorBlock day = "Monday"/>
          <DaySelectorBlock day = "Tuesday"/>
          <DaySelectorBlock day = "Wednesday"/>
          <DaySelectorBlock day = "Thursday"/>
          <DaySelectorBlock day = "Friday"/>
          <DaySelectorBlock day = "Saturday" />
        </div>
      );
  }
}
