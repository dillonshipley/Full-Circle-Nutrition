import React, { Component } from 'react';

class ScheduleInfo extends Component{
  render(){
    return (
      <div className = "scheduleCardContainer">
        <div className = "card" id = "standardScheduleCard">
          <div className = "cardSpacer"></div>
          <div className = "cardTitle">STANDARD</div>
          <div className = "cardInfoText">3 meals, 1 snack. Like clockwork.</div>
        </div>
        <div className = "card" id = "templateScheduleCard">
          <div className = "cardSpacer"></div>
          <div className = "cardTitle">SOME REPEATS</div>
          <div className = "cardInfoText">Build a template used over a few days. Customize the rest.</div>
        </div>
        <div className = "card" id = "funkyScheduleCard">
        <div className = "cardSpacer"></div>
          <div className = "cardTitle">100% CUSTOM</div>
          <div className = "cardInfoText">So your life's chaotic, huh?</div>
        </div>
      </div>
    );
  }
}

export default ScheduleInfo;
