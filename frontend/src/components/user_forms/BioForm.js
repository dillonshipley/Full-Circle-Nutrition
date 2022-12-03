import React, { Component, useState } from 'react';
import MacroCalculator from '../tools/MacroCalculator';
import TextInput from '../utilities/TextInput';
import Option from '../utilities/Option'

import './BioForm.css';

const ids = ["sexInput", "activityInput", "goalInput"]
const sexOptions = ['', 'Male', 'Female'];
const activityOptions = ['', "Sedentary", "Lightly Active", "Moderately Active", "Active", "Very Active"];
const goalOptions = [
'', 'Rapid Loss', 'Moderate Loss', 'Slight Loss', 'Neutral','Slight Gain','Moderate Gain', 'Rapid Gain'
];

class BioForm extends Component{
  constructor(props){
    super(props);
    this.state = {
      macros: [],
      weightType: "LB",
      heightType: "IN"
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

  changeSelection(type, value){
    switch(type){
      case "weight":
        console.log(value);
        this.setState({weightType: value});
        break;
      case "height":
        console.log(value);
        this.setState({heightType: value});
        break;
      default:
        break;
    }
  }

  change(type, value){
    switch(type){
      case "weight":
        this.setState({weight: value});
        break;
      case "height":
        this.setState({height: value});
        break;
      case "age":
        this.setState({age: value});
        break;
      case "sex":
        this.setState({sex: value});
        break;
      case "activity":
        this.setState({activity: value});
        break;
      case "goal":
        this.setState({goal: value});
        break;
    }
  }

  calculateMacros(){

    let valueData = [this.state.weight, this.state.height, this.state.age, this.state.sex, this.state.activity, this.state.goal]
    ids.forEach(element => valueData.push(document.getElementById(element).value))

    const typeData = [];
    typeData.push(this.state.weightType);
    typeData.push(this.state.heightType);

    this.setState({loading: true});
    var macroArray = MacroCalculator(valueData, typeData);
    this.setState({macros: macroArray}, () => {
        this.setState({loading: false});
    });
    this.props.forward(macroArray);
  }

  render(){
    return (
      <div id = "BioFormScreen">
        <div id = "NLBioFormContainer">
          <div id = "BioFormLeftColumn" className = "BioFormColumn">
            <p className = "BioFormLabel">Information About Your Body</p>
            <TextInput type = "Weight" options = {["LB", "KG"]} setVal = {(e) => this.change("weight", e)} setType = {(e) => this.changeSelection("weight", e)}/>
            <TextInput type = "Height" options = {["IN", "CM"]} setVal = {(e) => this.change("height", e)} setType = {(e) => this.changeSelection("height", e)}/>
            <TextInput type = "Age" setVal = {(e) => this.change("age", e)} options = {null}/>
            <Option setVal = {(e) => this.change("sex", e)} vals = {sexOptions} name = {"sex"}/>
          </div>
          <div id= "BioFormRightColumn" className = "BioFormColumn">
            <p className = "BioFormLabel">Information About Your Habits</p>
            <Option setVal = {(e) => this.change("sex", e)} vals = {activityOptions} name = {"activity"} />
            <Option setVal = {(e) => this.change("sex", e)} vals = {goalOptions} name = {"goal"} />
          </div>
          </div>
      <button className = "SaveButton" onClick = {() => this.calculateMacros()}>Save</button>
      <button className = "LoginButton" onClick = {() => this.prePopulate()}>Login or Create an Account</button>
      </div>
    );
  }
}

export default BioForm;
