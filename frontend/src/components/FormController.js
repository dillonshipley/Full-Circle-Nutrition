import BioForm from './user_forms/BioForm';
import ScheduleForm from './user_forms/ScheduleForm'
import PreferencesForm from './user_forms/PreferencesForm'
import React, { Component } from 'react';
import ProgressBar from './utilities/ProgressBar';
import Results from './Results'

class FormController extends Component {

  constructor(props){
    super(props);
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
  }

  display(){
    switch(this.state.step){
      case 1:
        return <BioForm forward = {(e) => this.advance(e)}/>
      case 2:
        return <ScheduleForm macros = {this.state.macros} forward = {(e) => this.advance(e)}/>;
      case 3:
        return <PreferencesForm forward = {(e) => this.advance(e)}/>
      case 4:
        return <Results />
      default:
        return <div>ERROR</div>;
    }
  }

  render(){
    return (
      <div>
        <div id = "formControllerHeader">
          <button className = "backButton" onClick = {this.props.back}>Back</button>
          <ProgressBar className = "progressBar" step = {this.state.step} />
        </div>
        <div id = "formControllerBody">
          {this.display()}
        </div>
      </div>
      );

  }
}

export default FormController;
