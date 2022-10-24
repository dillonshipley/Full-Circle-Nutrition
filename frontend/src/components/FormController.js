import BioForm from './user_forms/BioForm';
import ScheduleInfo from './user_forms/ScheduleInfo'
import React, { Component } from 'react';
import ProgressBar from './utilities/ProgressBar';
import Results from './Results'

class FormController extends Component {

  constructor(props){
    super(props);
    const progess = ["logon"];
    this.state = JSON.parse(localStorage.getItem('formState')) || {
      logon: false,
      recipe_complete: true,
      step: 1
    }
  }

  componentDidMount(){
    document.getElementById("PB1").classList.add("inProgress");
  }

  advance(props){
    var current = this.state.step;
    switch(current){
      case 1:
        this.setState({macros: props}, () => this.setState({step: current + 1}));
        this.setState({step: current + 1});
        break;
      case 2:
        this.setState({schedule: props}, () => this.setState({step: current + 1}));
        this.setState({step: current + 1});
        break;
      default:
        this.setState({step: current + 1});
        break;
    }
    document.getElementById("PB" + current).classList.remove("inProgress");
    document.getElementById("PB" + current).classList.add("completed");
    localStorage.setItem('formState', JSON.stringify(this.state));
    document.getElementById("PB" + (current + 1)).classList.add("inProgress");
  }

  display(){
    switch(this.state.step){
      case 1:
        return <BioForm forward = {(e) => this.advance(e)}/>
      case 2:
        return <ScheduleInfo macros = {this.state.macros} forward = {(e) => this.advance(e)}/>;
      case 3:
        return <Results macros = {this.state.macros} schedule_info = "y" />
    }
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
