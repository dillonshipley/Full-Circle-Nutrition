import React, {useState} from 'react';

export default function TextInput(props){
  const [val, setVal] = useState(0);

  function setValWrapper(){

    let value = document.getElementById(props.type + "TextInput").value;
    props.change(value);
    setVal(value);
  }

  return(
    <div id = {"current" + props.type} className = "InputContainer">
        <div id = {props.type + "InputLabel"} className = "InputLabel">{props.label}</div>
        <input type = "text" maxLength = "20" onChange = {() => setValWrapper()} id = {props.type + "TextInput"} className="textInput"></input>
     </div>
  );
}
