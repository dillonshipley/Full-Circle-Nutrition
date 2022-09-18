import LogonBioForm from './user_forms/LogonBioForm';
import NonLogonBioForm from './user_forms/NonLogonBioForm';
import ScheduleInfo from './user_forms/ScheduleInfo'
import React, { Component } from 'react';


function Logon(props){
  if(props.logon)
    return <LogonBioForm bio_info = "x" />
  else
    return <NonLogonBioForm bio_info = "x" />
}

class FormController extends Component {

  constructor(props){
    super(props);
    this.state = {
      logon: false,
      recipe_complete: true
    }
  }

  returnResults(props){
    if(this.state.recipe_complete){
      return (
        <div>oof</div>
        //<Results bio_info = "X" schedule_info = "y" />
      );
    }
  }

  render(){
    return (
      <div id = "logonDeterminer">
        <Logon logon = {this.state.logon} />
        <ScheduleInfo schedule_info = "x" />
        {/*this.returnResults()*/}
      </div>
      );

  }
}

export default FormController;
