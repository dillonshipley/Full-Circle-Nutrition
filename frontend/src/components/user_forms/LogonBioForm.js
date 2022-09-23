import React, { Component } from 'react';
import MacroCalculator from '../tools/MacroCalculator';

class LogonBioForm extends Component{

  constructor(props){
    super(props);
    this.state = {

    }
  }

  componentDidMount(){
    this.getLogonInfo();
  }

  getLogonInfo(){
    //get user data here
  }

  render(){
    return (
      <div>
        <div id = "firstName">
            insert first name text box
        </div>
        <div id = "lastName">
        </div>
        <div id = "height">
        </div>
        <div id = "currentWeight">
        </div>
        <div id = "bodyFat">
        </div>
      </div>
    );
  }
}

export default LogonBioForm;
