import React, { Component } from 'react';
import MacroCalculator from '../tools/MacroCalculator';

function TextInput(props){
  return (
    <div id = {"current" + props.type}>
    <p className = "InputLabel">Please enter your current {props.type}:</p>
    <input type = "text" id = {props.type + "Input"} name = {props.type} className = "textInput"/>
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

  calculateMacros(){
    var weight = document.getElementById("weightInput").value;
    var height = document.getElementById("heightInput").value;
    var age = document.getElementById("ageInput").value
    var sex = document.getElementById("sexInput").value;
    if(weight === '' || height === '' || age === '' || sex === '') {
      this.error();
      return;
    }
    this.setState({loading: true});
    console.log(document.getElementById("weightInput").value);
    const data = [
      parseInt(document.getElementById("weightInput").value),
      parseInt(document.getElementById("heightInput").value),
      parseInt(document.getElementById("ageInput").value),
      document.getElementById("sexInput").value,
    ]
    console.log(data);

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
          <TextInput type = "weight" />
          <TextInput type = "height" />
          <TextInput type = "age" />
          <div id = "sex">
            <p className = "InputLabel">Please enter your sex:</p>
            <select name = "sex" id = "sexInput" className = "textInput">
              <option value = ""></option>
              <option value = "M">Male</option>
              <option value = "F">Female</option>
            </select>
          </div>
        </form>
        <button className = "SaveButton" onClick = {() => this.calculateMacros()}>Save</button>

      </div>
    );
  }
}

export default NonLogonBioForm;
