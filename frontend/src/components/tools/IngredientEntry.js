import React, {Component} from 'react';
import TextInput from '../utilities/inputs/TextInput';
import DigitInput from '../utilities/inputs/DigitInput';

import './Tools.css';

export default class IngredientEntry extends Component{
    constructor(props){
        super(props);
        this.state = {name: "hello"};
    }

    change(type, value){
      switch(type){
        case "name":
          this.setState({name: value});
          break;
        case "cals":
          this.setState({cals: value});
          break;
        case "carbs":
          this.setState({carbs: value});
          break;
        case "fat":
          this.setState({fat: value});
          break;
        case "protein":
          this.setState({protein: value});
          break;
        default:
          break;
      }
    }

    print(){
      let object = {"name" : this.state.name,
      "vegetarian": "True",
      "calories": this.state.cals,
      "fat": this.state.fat,
      "protein" : this.state.protein,
      "units": 1}
      console.log(object);
      //fetch(resource, {"method": "POST", "body": object})
      /*fetch('/pathways')
        .then((res) => res.json())
        .then(data => {
          this.setData(data)
      }, []);*/
    }

    render(){
      return (
        <div id = "ingredientEntryContainer">
          <h4>Enter a new ingredient!</h4>
          <TextInput type = "name" label = "Ingredient Name" change = {(e) => this.change("name", e)}/>
          <DigitInput type = "Calories" setVal = {(e) => this.change("cals", e)} n = {4} settings = {"condense"} />
          <DigitInput type = "Carbs" setVal = {(e) => this.change("carbs", e)} n = {3} settings = {"condense"}/>
          <DigitInput type = "Protein" setVal = {(e) => this.change("protein", e)} n = {3} settings = {"condense"}/>
          <DigitInput type = "Fat" setVal = {(e) => this.change("fat", e)} n = {3} settings = {"condense"}/>
          <button onClick = {() => this.print()} id = "saveIngredientButton">Save Ingredient!</button>
        </div>
      );
    }
}
