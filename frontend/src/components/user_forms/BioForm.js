import React, { Component } from 'react';
import MacroCalculator from '../tools/MacroCalculator';
import TextInput from '../utilities/TextInput'

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

const ids = ["weightInput", "heightInput", "ageInput", "sexInput", "activityInput", "goalInput"]



function Option(props){
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

  return (
    <div className = "OptionContainer">
      <p className = "InputLabel">{label}</p>
      <select name = {props.name} id = {props.name + "Input"} className = "textInput">
        {mappingObject.map(({value, text}, index) => <option key = {text} value = {value}>{text}</option>)}
      </select>
    </div>
  );
}

class BioForm extends Component{
  constructor(props){
    super(props);
    this.state = {
      macros: [],
      loading: false,
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
    const valueData = [];
    for(let i = 0; i < ids.length; i++){
      let element = document.getElementById(ids[i]);
      if(element.value === ''){
        this.error();
        return;
      } else {
        if(isNaN(element.value))
          valueData.push(element.value);
        else
          valueData.push(parseInt(element.value));
      }
    }

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
            <TextInput type = "Weight" options = {["LB", "KG"]} setType = {(e) => this.changeSelection(e)}/>
            <TextInput type = "Height" options = {["IN", "CM"]} setType = {(e) => this.changeSelection(e)}/>
            <TextInput type = "Age" options = {null}/>
            <Option name = {"sex"}/>
          </div>
          <div id= "BioFormRightColumn" className = "BioFormColumn">
            <p className = "BioFormLabel">Information About Your Habits</p>
            <Option name = {"activity"} />
            <Option name = {"goal"} />
          </div>
          </div>
      <button className = "SaveButton" onClick = {() => this.calculateMacros()}>Save</button>
      <button className = "LoginButton" onClick = {() => this.prePopulate()}>Login or Create an Account</button>
      </div>
    );
  }
}

export default BioForm;
