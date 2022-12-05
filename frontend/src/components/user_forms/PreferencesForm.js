import React, {Component} from 'react';
import FlavorProfile from '../utilities/FlavorProfile'


let availableFlavors = ["Mexican", "Greek", "Italian"]


class PreferencesForm extends Component {

  constructor(props){
    super(props);
    this.state = {
      type1: availableFlavors[0],
      type2: availableFlavors[1]
    }
  }

  render(){
    return(
      <div id = "preferencesFormContainer">
        <FlavorProfile type = {this.state.type1} num = "1" />
        <FlavorProfile type = {this.state.type2} num = "2" />
      </div>
    );
  }

}

export default PreferencesForm;
