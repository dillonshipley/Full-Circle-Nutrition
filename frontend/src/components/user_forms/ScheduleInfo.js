import React, { Component } from 'react';

function Card(props){
    return (
    <div className = "card scheduleCard" id = {"scheduleCard" + props.num} onClick = {props.onClick}>
      <div className = "cardIcon">
        //insert icon here
      </div>
      <div>
        <div className = "cardSpacer"></div>
        <div className = "cardTitle">{props.title}</div>
        <div className = "cardInfoText">{props.text}</div>
      </div>
    </div>
  );
}

class ScheduleInfo extends Component{

  constructor(props){
    super(props);
    this.state = {
      display: "start",
      macros: props.macros
    }
  }

  setScheduleType(type){
    switch(type){
      case 1:
        this.state.meals = [14, 7, 7];
        this.props.forward(this.state.meals);
        break;
      case 2:
        break;
      case 3:
        break;
    }
    return;
  }

  render(){
    switch(this.state.display){
      case "start":
        return (
          <div className = "scheduleCardContainer">
            <Card onClick = {(e) => this.setScheduleType(1)} title = "STANDARD" text = "3 meals, 1 snack. Like clockwork."/>
            <Card onClick = {(e) => this.setScheduleType(2)} title = "SOME REPEATS" text = "Build a template used over a few days. Customize the rest."/>
            <Card onClick = {(e) => this.setScheduleType(3)} title = "100% CUSTOM" text = "Every day is different-ish"/>
          </div>
        );
      default:
        break;
    }


  }
}

export default ScheduleInfo;
