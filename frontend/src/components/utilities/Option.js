import React, {useState, useEffect} from 'react';

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
  })

  const change = event => {
    console.log(event.target.value);
    props.setVal(event.target.value);
  }

  return (
    <div className = "OptionContainer">
      <p className = "InputLabel">{label}</p>
      <select onChange = {change} name = {props.name} id = {props.name + "Input"} className = "textInput">
        {props.vals.map(option => (
          <option key = {option} value = {option}>{option}</option>
        ))}
      </select>
    </div>
  );
}
