import LogonBioForm from './user_forms/LogonBioForm';
import NonLogonBioForm from './user_forms/NonLogonBioForm';
import ScheduleInfo from './user_forms/ScheduleInfo'
import Results from './Results'
import React, { Component } from 'react';


function returnResults(props){
  if(this.state.recipe_complete){
    return (
      <Results bio_info = "X" schedule_info = "y" />
    );
  }
}

class FormController extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      logon: true,
      recipe_complete: true
    }
  }

  render(){
    if(this.state.logon == true){
      return (
        <div>
          <LogonBioForm bio_info = "x" />
          <ScheduleInfo schedule_info = "x" />
          {returnResults()}
        </div>
      );
    } else {
      return (
        <div>
        <NonLogonBioForm bio_info = "x" />
        <ScheduleInfo schedule_info = "x" />
        {returnResults()}
        }
        </div>
      );
    }
  }
}

export default FormController;
