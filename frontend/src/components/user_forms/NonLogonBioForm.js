import React, { Component, useState, useEffect } from 'react';
import MacroCalculator from '../tools/MacroCalculator';

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

function Selector(props){
  const [optionSelected, setOptionSelected] = useState("");

  function setSelectedWrapper(value){
    if(optionSelected != null)
      document.getElementById(optionSelected).classList.remove("selected");
    if(optionSelected = value + "Option"){
      setOptionSelected = null;
      return;
    }
    document.getElementById(value + "Option").classList.add("selected");
    setOptionSelected(value + "Option");
    props.setType({type: props.type + "Type", option: value})
    console.log(value);
    console.log(optionSelected);
  }

  return (
    <div className = "selectorContainer">
        {props.options?.map(option => (
          <div id = {option + "Option"} className = "selectorOption" key = {option} onClick = {(e) => setSelectedWrapper(option)}>{option}</div>
        ))}
    </div>
  );
}

function TextInput(props){
  if(props.options === null){
    return (
      <div id = {"current" + props.type}>
        <p className = "InputLabel">Please enter your current {props.type}:</p>
        <input type = "text" id = {props.type + "Input"} name = {props.type} className = "textInput"/>
      </div>
    );
  } else {
    return (
      <div id = {"current" + props.type}>
        <p className = "InputLabel">Please enter your current {props.type}:</p>
        <input type = "text" id = {props.type + "Input"} name = {props.type} className = "textInput"/>
        <Selector options = {props.options} type = {props.type} setType = {props.setType}/>
      </div>
    );
  }
}

function Option(props){
  var mappingObject = null;
  var label = "";

  switch(props.name){
    case "sex":
      mappingObject = sexOptions;
      label = "Please enter your sex:";
      break;
    case "activity":
      mappingObject = activityOptions;
      label = "Please enter your activity level:";
      break;
    case "goal":
      mappingObject = goalOptions;
      label = "Please enter your current goal:"
      break;
    default:
      break;
  }

  return (
    <div>
      <p className = "InputLabel">{label}</p>
      <select name = {props.name} id = {props.name + "Input"} className = "textInput">
        {mappingObject.map(({value, text}, index) => <option key = {text} value = {value}>{text}</option>)}
      </select>
    </div>
  );
}

class NonLogonBioForm extends Component{
  constructor(props){
    super(props);
    this.state = {
      data: props.data,

      macros: [],
      loading: false
    }
  }

  error(){
    var collection = document.getElementsByClassName("textInput")
    for(const x of collection) {
      if(x.value === ''){
        x.style.backgroundColor = "#ffa7a7";
        x.style.border = "1px solid black";
      }
    }
  }

  changeSelection(props){
    switch(props.type){
      case "weightType":
        this.setState({weightType: props.option});
        break;
      case "heightType":
        this.setState({heightType: props.option});
        break;
      default:
        break;
    }
  }

  prePopulate(){
    document.getElementById("weightInput").value = 195;
    document.getElementById("heightInput").value = 71;
    document.getElementById("ageInput").value = 21;
    document.getElementById("sexInput").value = 'M';
    document.getElementById("activityInput").value = '1.2';
    document.getElementById("goalInput").value = 'rloss';
  }

  calculateMacros(){
    var weight = [document.getElementById("weightInput").value, this.state.weightType];
    var height = document.getElementById("heightInput").value;
    var age = document.getElementById("ageInput").value
    var sex = document.getElementById("sexInput").value;
    var activity = document.getElementById("activityInput").value;
    var goal = document.getElementById("goalInput").value;
    if(weight[0] === '' || height === '' || age === '' || sex === '' || activity === '' || goal === '') {
      this.error();
      return;
    }
    this.setState({loading: true});
    console.log(document.getElementById("weightInput").value);
    const data = [parseInt(weight[0]), weight[1], parseInt(height), parseInt(age), sex, parseFloat(activity), goal]

    var macroArray = MacroCalculator(data);
    this.setState({macros: macroArray}, () => {
        this.setState({loading: false});
    });
    this.props.back();
  }

  render(){
    return (
      <div id = "NLBioFormContainer">
        <form>
          <TextInput type = "weight" options = {["LB", "KG"]} setType = {(e) => this.changeSelection(e)}/>
          <TextInput type = "height" options = {["IN", "CM"]} setType = {(e) => this.changeSelection(e)}/>
          <TextInput type = "age" options = {null}/>
          <Option name = {"sex"}/>
          <Option name = {"activity"} />
          <Option name = {"goal"} />
        </form>
        <button className = "SaveButton" onClick = {() => this.calculateMacros()}>Save</button>
        <button className = "LoginButton" onClick = {() => this.prePopulate()}>Login or Create an Account</button>
      </div>
    );
  }
}

export default NonLogonBioForm;
