import React, {Component} from 'react';

function Counter(props){
  return (
    <div className = "counterContainer">
      <div className = "counterDiv counterDivSymbol" onClick = {(e) => props.down(props.type)}>-</div>
      <div className = "counterDiv">{props.num}</div>
      <div className = "counterDiv counterDivSymbol" onClick = {(e) => props.up(props.type)}>+</div>
    </div>
  );
}

class DaySelectorBlock extends Component{

  constructor(props){
    super(props);
    this.state = {
      MPD: 3,
      breakfast: false,
      SPD: 1
    }
  }

  increase(props){
    if(props === "MPD") {
      this.setState({MPD: this.state.MPD + 1});
      this.props.increase("MPD");
    } else if (props === "SPD") {
      this.setState({SPD: this.state.SPD + 1});
      this.props.increase("SPD");
    }
  }

  error(){

  }

  decrease(props){
    if(props === "MPD"){
      if(this.state.MPD === 0){
        this.error();
        return;
      }
      this.setState({MPD: this.state.MPD - 1});
      this.props.decrease("MPD");
    } else if (props === "SPD") {
      if(this.state.SPD === 0){
        this.error();
        return;
      }
      this.setState({SPD: this.state.SPD - 1});
      this.props.decrease("SPD");
    }
  }

  render(){
    return (
      <div className = "daySelectorCB">
        <div className = "dayLabel">{this.props.day}</div>
        <Counter className = "counter" num = {this.state.MPD} type = "MPD" down = {(e) => this.decrease(e)} up = {(e) => this.increase(e)} />
        <Counter className = "counter" num = {this.state.SPD} type = "SPD" down = {(e) => this.decrease(e)} up = {(e) => this.increase(e)} />
        <input type = "checkbox"></input>
        <input type = "checkbox"></input>
      </div>
    )
  }
}

export default DaySelectorBlock;
