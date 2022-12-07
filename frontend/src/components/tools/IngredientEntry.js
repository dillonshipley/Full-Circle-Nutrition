import React, {Component} from 'react';
import TextInput from '../utilities/inputs/TextInput';

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
        default:
          break;
      }
    }

    print(){
      console.log(this.state.name);
    }

    render(){
      return (
        <div id = "ingredientEntryContainer">
          <TextInput type = "name" label = "Ingredient Name" change = {(e) => this.change("name", e)}/>
          <button onClick = {() => this.print()}>clickme</button>
        </div>
      );
    }
}
