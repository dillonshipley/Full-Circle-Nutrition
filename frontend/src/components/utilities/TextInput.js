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
    <div className = {divClass}>
      {[...Array(props.n)].map((e, i) => <input type = "text" maxLength = "1" id = {props.type + "DigitInput" + i} className="digitInput" key={i}></input>)}
    </div>
  );
}

export default function TextInput(props){
  const [n, setN] = useState(() => {
    switch(props.type){
      case "Weight":
        return 3;
      case "Height":
        return 2;
      case "Age":
        return 2
    }
  });

  const [val, setVal] = useState(0);

  return(
    <div id = {"current" + props.type} className = "InputContainer">
      <p className = "InputLabel">{props.type}</p>
      <InputBlock type = {props.type} edit = {(e) => {setVal(e); props.setVal(e)}}className = "digitContainer" n = {n} />
     {(props.options != null) && <Selector options = {props.options} type = {props.type} setType = {(e) => props.setType(e)}/>}
     </div>
  );
}
