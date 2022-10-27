import React, { useState, useEffect } from 'react';

function Segment(props){
  if(props.num < props.selected){
    return <div id = {"PB" + props.num} className = "progressBarSegment completed"></div>
  } else if (props.num === props.selected){
    return <div id = {"PB" + props.num} className = "progressBarSegment inProgress"></div>
  } else {
    return <div id = {"PB" + props.num} className = "progressBarSegment"></div>  
  }
}

function ProgressBar(props) {

  /*
  const [step, setStep] = useState(props.step);
  let length = 3;

  useEffect(() => {console.log(props.step)})
*/
  return (
    <div className = "progressBarContainer">
      <div id = "progressBarLabel">Progress</div>
      <div id = "progressBarSubdivider">
        <Segment num = {1} selected = {props.step} />
        <Segment num = {2} selected = {props.step} />
        <Segment num = {3} selected = {props.step} />
      </div>
    </div>
  );
}

export default ProgressBar;
