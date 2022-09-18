import React, { Component } from 'react';

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

  }

  render(){
    return (
      <div>
        {this.getLogonInfo()}
        <div id = "firstName">
            //style: text box
        </div>
        <div id = "lastName">
            //style: text box
        </div>
        <div id = "height">
            //style: slider
        </div>
        <div id = "currentWeight">
            //style: text box
        </div>
        <div id = "bodyFat">
            //style: dropdown (optional, rough estimate)
        </div>
      </div>
    );
  }
}

export default LogonBioForm;
