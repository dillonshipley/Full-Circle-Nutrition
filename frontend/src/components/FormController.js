import LogonBioForm from './user_forms/LogonBioForm';
import NonLogonBioForm from './user_forms/NonLogonBioForm';
import ScheduleInfo from './user_forms/ScheduleInfo'
import React, { Component } from 'react';
import ProgressBar from './utilities/ProgressBar';
import Results from './Results'

function BioForm(props){
  if(props.logon)
    return <LogonBioForm bio_info = "x" />
  else
    return <NonLogonBioForm bio_info = "x" back = {props.back}/>
}

class FormController extends Component {

  constructor(props){
    super(props);
    const progess = ["logon"]
    this.state = {
      logon: false,
      recipe_complete: true, 
      step: 1
    }
  }

  componentDidMount(){
    document.getElementById("PB1").classList.add("inProgress");
  }

  advance(){
    var current = this.state.step;
    document.getElementById("PB" + current).classList.remove("inProgress");
    document.getElementById("PB" + current).classList.add("completed");
    this.setState({step: current + 1});
    document.getElementById("PB" + (current + 1)).classList.add("inProgress");
  }

  display(){
    if(this.state.step === 1)
      return <BioForm logon = {this.state.logon} back = {() => this.advance()}/>
    else if(this.state.step === 2)
      return <ScheduleInfo schedule_info = "x" />
    else if(this.state.step === 3)
      return <Results bio_info = "X" schedule_info = "y" />

    //TODO --- include preferences bit
    
  }

  render(){
    return (
      <div>
        <div id = "formControllerHeader">
          <button className = "backButton" onClick = {this.props.back}>Back</button>
          <ProgressBar className = "progressBar" progress = {this.state.progress} />
        </div>
        <div id = "formControllerBody">
          {this.display()}
        </div>
      </div>
      );

  }
}

export default FormController;
