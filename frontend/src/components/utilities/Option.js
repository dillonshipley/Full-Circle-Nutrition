import React, {useState} from 'react';

const sexOptions = [{value: '', text: ''}, {value: 'M', text: 'Male'}, {value:'F', text: 'Female'}];
const activityOptions = [{value: '', text: ''}, {value: "1.2", text: "Sedentary"}, {value: "1.375", text: "Lightly Active"}, {value: "1.55", text: "Moderately Active"}, {value: "1.725", text: "Active"}, {value: "1.9", text: "Very Active"}];
const goalOptions = [
  {value: '', text: ''},
  {value: 'rloss', text: 'Rapid Loss'},
  {value:'mloss', text: 'Moderate Loss'},
  {value:'sloss', text: 'Slight Loss'},
  {value:'netural', text: 'Neutral'},
  {value:'sgain', text: 'Slight Gain'},
  {value:'mgain', text: 'Moderate Gain'},
  {value:'rgain', text: 'Rapid Gain'}
];

export default function Option(props){
  const [val, setVal] = useState('');
  var mappingObject = null;
  var label = "";

  switch(props.name){
    case "sex":
      mappingObject = sexOptions;
      label = "Sex";
      break;
    case "activity":
      mappingObject = activityOptions;
      label = "Activity Level:";
      break;
    case "goal":
      mappingObject = goalOptions;
      label = "Current Goal:"
      break;
    default:
      break;
  }


  const change = event => {
    console.log(event.target.value);
    props.setVal(event.target.value);
  }

  return (
    <div className = "OptionContainer">
      <p className = "InputLabel">{label}</p>
      <select onChange = {change} name = {props.name} id = {props.name + "Input"} className = "textInput">
        {mappingObject.map(option => (
          <option key = {option.text} value = {option.value}>{option.text}</option>
        ))}
      </select>
    </div>
  );
}
