import React, { useState, useEffect } from 'react';

function Segment(props){
  if(props.num < props.selected){
    return <div id = {"PB" + props.num} className = "progressBarSegment completed"
  }
}

function ProgressBar(props) {

  const [step, setStep] = useState(0);
  let length = 3;

  function setStepWrapper(stepParam){

  }

  useEffect(() => {
    setStep(2);
    console.log(props.step)
  });

  return (
    <div className = "progressBarContainer">
      <div id = "progressBarLabel">Progress</div>
      <div id = "progressBarSubdivider">
        <div id = "PB1" className = "progressBarSegment"></div>
        <div id = "PB2" className = "progressBarSegment"></div>
        <div id = "PB3" className = "progressBarSegment"></div>
      </div>
    </div>
  );
}

export default ProgressBar;
