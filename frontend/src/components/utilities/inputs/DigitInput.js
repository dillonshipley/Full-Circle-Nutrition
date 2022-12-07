import React, {useState, useEffect} from 'react';
import Selector from './Selector'

function concatVals(num, type){
  let myVal = 0
  for(let j = 0; j < num; j++){
    let digitVal = parseInt(document.getElementById(type + "DigitInput" + j).value);
    myVal = myVal + digitVal * (10 ** (num - j - 1));
  }
  console.log(myVal);
  return myVal;
}

function InputBlock(props){

  const [val, setVal] = useState(0);

  useEffect(() => {
      var container = document.getElementsByClassName(props.type + "DigitContainer")[0];
      container.onkeyup = function(e) {
        var target = e.target;
        var maxLength = parseInt(target.attributes["maxlength"].value, 10);
        var myLength = target.value.length;
        if (myLength >= maxLength) {
          var next = target.nextElementSibling;
          if (next == null){
              let value = concatVals(props.n, props.type);
              setVal(value);
              props.edit(value)
          }else
                next.focus();
      }
    // Move to previous field if empty (user pressed backspace)
      else if (myLength === 0) {
          var previous = target;
          while (previous = previous.previousElementSibling) {
            if (previous == null)
                break;
            if (previous.tagName.toLowerCase() === "input") {
                previous.focus();
                break;
            }
        }
      }
    }
  });

  let divClass = props.type + "DigitContainer digitContainer"

  return (
    <div id = {props.type + "Container"} className = {divClass}>
      {[...Array(props.n)].map((e, i) => <input type = "text" maxLength = "1" id = {props.type + "DigitInput" + i} className="digitInput" key={i}></input>)}
    </div>
  );
}

export default function DigitInput(props){
  const [label, setLabel] = useState(() => {
    switch(props.type){
      case "Weight":
        return props.type;
      case "Height":
        return props.type;
      case "Age":
        return props.type;
      case "firstDayMeals":
        return "How many meals will you eat after finishing prep?";
      default:
        return props.type;
    }
  });

  useEffect(() => {
    if(props.settings != null){
      if(props.settings.includes("wholeline")){
        document.getElementById("current" + props.type).classList.add("wholeline");
        document.getElementById(props.type + "InputLabel").classList.add("wholeline");
        document.getElementById(props.type + "Container").classList.add("wholeline");
      }
      if(props.settings.includes("condense")){
        document.getElementById(props.type + "InputLabel").classList.add("condense");
        document.getElementById(props.type + "Container").classList.add("condense");
      }
  }});

  const [val, setVal] = useState(0);

  return(
    <div id = {"current" + props.type} className = "InputContainer">
      <div id = {props.type + "InputLabel"} className = "InputLabel">{label}</div>
      <InputBlock type = {props.type} edit = {(e) => {setVal(e); props.setVal(e)}} id = {props.type + "Container"} className = "digitContainer" n = {props.n} />
     {(props.options != null) && <Selector options = {props.options} type = {props.type} setType = {(e) => props.setType(e)}/>}
     </div>
  );
}
