import React, {Component} from 'react';
import IngredientEntry from './IngredientEntry';

export default class AdminTools extends Component{
    constructor(props){
        super(props);
        this.state = {};
    }

    change(type, value){
      switch(type){
        case "name":
          this.setState({name: value});
      }
    }

    render(){
      return (
        <div id = "adminToolsContainer">
            <IngredientEntry />
            <div id = "recipeBuilderContainer">
            </div>
        </div>
      );
    }
}
