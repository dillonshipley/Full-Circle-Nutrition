import React, { Component } from 'react';
import Slider from '@mui/material/Slider';
import MacroCalculator from '../tools/MacroCalculator';

const heightArray = [
  {
    value: 58,
    label: "4'10"
  },
  {
    value: 59,
    label: "4'11"
  },
  {
    value: 60,
    label: "5'0"
  },
  {
    value: 61,
    label: "5'1"
  },
  {
    value: 62,
    label: "5'2"
  },
  {
    value: 63,
    label: "5'3"
  },
  {
    value: 64,
    label: "5'5"
  },
  {
    value: 65,
    label: "5'4"
  },
  {
    value: 66,
    label: "5'6"
  },
  {
    value: 67,
    label: "5'7"
  },
  {
    value: 68,
    label: "5'8"
  },
  {
    value: 69,
    label: "5'9"
  },
  {
    value: 70,
    label: "5'10"
  },
  {
    value: 71,
    label: "5'11"
  },
  {
    value: 72,
    label: "6'0"
  }
]

class NonLogonBioForm extends Component{
  constructor(props){
    super(props);
    this.state = {
      data: props.data,
      macros: [],
      loading: false
    }
  }

  calculateMacros(){
    this.setState({loading: true});
    const data = [
      parseInt(document.getElementById("weightInput").value),
      parseInt(document.getElementById("heightInput").value),
      parseInt(document.getElementById("ageInput").value),
      document.getElementById("sexInput").value,
    ]
    console.log(data);

    var macroArray = MacroCalculator("y");
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
        <div id = "currentWeight">
            <p className = "InputLabel">Please enter your current weight:</p>
            <input type = "text" id = "weightInput" name = "weight" className = "textInput"/>
            <p> TODO: KG / LBS </p>
        </div>
          <div id = "currentWeight">
            <p className = "InputLabel">Select your height:</p>
            <div className = "heightSlider">
              <Slider
              size="medium"
              min ={58}
              max = {72}
              defaultValue={70}
              aria-label="Small"
              valueLabelDisplay="off"
              step = {null}
              marks = {heightArray}
              id = "heightInput"
              />
            </div>
          </div>
          <div id = "currentAge">
              <p className = "InputLabel">Please enter your current age:</p>
              <input type = "text" id = "ageInput" name = "age" className = "textInput"/>
          </div>
          <div id = "sex">
            <p className = "InputLabel">Please enter your sex:</p>
            <select name = "sex" id = "sexInput" className = "textInput">
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
