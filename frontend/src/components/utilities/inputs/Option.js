import React, {useState, useEffect} from 'react';

import './Inputs.css';

export default function Option(props){
  const [val, setVal] = useState('');
  const [dictionary, setDictionary] = useState();
  const [label, setLabel] = useState("");

  useEffect(() => {
    switch(props.name){
      case "sex":
        setLabel("Sex");
        setDictionary(false);
        break;
      case "activity":
        setLabel("Activity Level:");
        break;
      case "goal":
        setLabel("Current Goal:");
        break;
      case "day":
        setLabel("What day are you most free to shop, cook, and prep on?");
        break;
      default:
        break;
    }
    if(props.settings != null && props.settings.includes("wholeline")){
      document.getElementById(props.name + "OptionDiv").classList.add("wholeline");
      document.getElementById(props.name + "OptionLabel").classList.add("wholeline");
    }
  })

  const change = event => {
    console.log(event.target.value);
    props.setVal(event.target.value);
  }

  return (
    <div id = {props.name  + "OptionDiv"}className = "OptionContainer">
      <div id = {props.name + "OptionLabel"} className = "InputLabel">{label}</div>
      <select onChange = {change} name = {props.name} id = {props.name + "Input"} className = "textInput">
        {props.vals.map(option => (
          <option key = {option} value = {option}>{option}</option>
        ))}
      </select>
    </div>
  );
}
