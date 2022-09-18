import LogonBioForm from './user_forms/LogonBioForm';
import NonLogonBioForm from './user_forms/NonLogonBioForm';
import ScheduleInfo from './user_forms/ScheduleInfo'
import Results from './Results'
import React, { Component } from 'react';




class FormController extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      logon: true,
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
    if(this.state.logon == true){
      return (
        <div>
          <div>hello!</div>
          <LogonBioForm bio_info = "x" />
          <ScheduleInfo schedule_info = "x" />
          {this.returnResults()}
        </div>
      );
    } else {
      return (
        <div>
        <div>hello!</div>
        <NonLogonBioForm bio_info = "x" />
        <ScheduleInfo schedule_info = "x" />
        {this.returnResults()}
        }
        </div>
      );
    }
  }
}

export default FormController;
