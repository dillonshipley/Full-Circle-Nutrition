import React, {useEffect} from 'react';
import Selector from './Selector'

function InputBlock(props){

  useEffect(() => {
      var container = document.getElementsByClassName(props.type + "DigitContainer")[0];
      container.onkeyup = function(e) {
        var target = e.srcElement || e.target;
        var maxLength = parseInt(target.attributes["maxlength"].value, 10);
        var myLength = target.value.length;
        if (myLength >= maxLength) {
          var next = target;
          while (next = next.nextElementSibling) {
            if (next == null)
                break;
            if (next.tagName.toLowerCase() === "input") {
                next.focus();
                break;
            }
          }
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
      {[...Array(props.n)].map((e, i) => <input type = "text" maxlength = "1" id = {props.type + "DigitInput" + i} className="digitInput" key={i}></input>)}
    </div>
  );
}

export default function TextInput(props){

  return(
    <div id = {"current" + props.type} className = "InputContainer">
      <p className = "InputLabel">{props.type}:</p>
      <InputBlock type = {props.type} className = "digitContainer" n = {3} />
     {(props.options != null) && <Selector options = {props.options} type = {props.type} setType = {props.setType}/>}

     </div>
  );
}
