import React, { Component } from 'react';
import MacroCalculator from '../tools/MacroCalculator';

function Selector(props){
  return (
    <div className = "selectorContainer">
        {props.options?.map(option => (
          <div className = "selectorOption" key = {option}>{option}</div>
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
        <Selector options = {props.options} />
      </div>
    );
  }
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

  calculateMacros(){
    var weight = [document.getElementById("weightInput").value, this.state.weight];
    var height = document.getElementById("heightInput").value;
    var age = document.getElementById("ageInput").value
    var sex = document.getElementById("sexInput").value;
    var activity = document.getElementById("activityInput").value;
    if(weight === '' || height === '' || age === '' || sex === '' || activity === '') {
      this.error();
      return;
    }
    this.setState({loading: true});
    console.log(document.getElementById("weightInput").value);
    const data = [parseInt(weight), parseInt(height), parseInt(age), sex, activity]

    var macroArray = MacroCalculator(data);
    this.setState({macros: macroArray}, () => {
        this.setState({loading: false});
    });
    this.props.back();
  }

  storeMacros(){
    console.log("works");
      //this.setState({macros: macros});
  }

  render(){
    return (
      <div id = "NLBioFormContainer">
        <form>
          <TextInput type = "weight" options = {["LB", "KG"]} />
          <TextInput type = "height" options = {["IN", "CM"]}/>
          <TextInput type = "age" options = {null}/>
          <div id = "sex">
            <p className = "InputLabel">Please enter your sex:</p>
            <select name = "sex" id = "sexInput" className = "textInput">
              <option value = ""></option>
              <option value = "M">Male</option>
              <option value = "F">Female</option>
            </select>
          </div>
          <div id = "activityLevel">
            <p className = "InputLabel">Please enter your activity level:</p>
            <select name = "activity" id = "activityInput" className = "textInput">
              <option value = ""></option>
              <option value = {1.2}>Sedentary</option>
              <option value = {1.375}>Lightly Active</option>
              <option value = {1.55}>Moderately Active</option>
              <option value = {1.725}>Active</option>
              <option value = {1.9}>Very Active</option>
            </select>
          </div>
          <div id = "goal">
            <p className = "InputLabel">Please enter your goal:</p>
            <select name = "activity" id = "activityInput" className = "textInput">
              <option value = ""></option>
              <option value = "rloss">Rapid Loss</option>
              <option value = "mloss">Moderate Loss</option>
              <option value = "sloss">Slight Loss</option>
              <option value = "neutral">Neutral</option>
              <option value = "sgain">Slight Gain</option>
              <option value = "mgain">Moderate Gain</option>
              <option value = "rgain">Rapid Gain</option>
            </select>
          </div>
        </form>
        <button className = "SaveButton" onClick = {() => this.calculateMacros()}>Save</button>

      </div>
    );
  }
}

export default NonLogonBioForm;
