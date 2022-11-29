import React, { Component } from 'react';
import DaySelectorBlock from '../utilities/DaySelectorBlock';
import './ScheduleForm.css';

class ScheduleForm extends Component{

  constructor(props){
    super(props);
    this.state = {
      display: "start",
      macros: props.macros,
      totalRegularMeals: 21,
      totalSnacks: 7,
      totalBreakfasts: 0
    }
  }

  increase(props){
    if(props === "MPD")
      this.setState({totalRegularMeals: this.state.totalRegularMeals + 1});
    else if (props === "SPD")
      this.setState({totalSnacks: this.state.totalSnacks + 1});
    else if(props === "Breakfasts")
      this.setState({totalBreakfasts: this.state.totalBreakfasts + 1});
  }

  decrease(props){
    if(props === "MPD")
      this.setState({totalRegularMeals: this.state.totalRegularMeals - 1});
    else if (props === "SPD")
      this.setState({totalSnacks: this.state.totalSnacks - 1});
    else if(props === "Breakfasts")
      this.setState({totalBreakfasts: this.state.totalBreakfasts - 1});
  }

  setCookDays(props){

  }

  finish(){
    var scheduleArray = [this.state.totalRegularMeals, this.state.totalSnacks, this.state.totalBreakfasts];
    this.props.forward(scheduleArray);
  }

  render(){
    return (
        <div>
            <table>
              <tr>
                <td className = "scheduleGridLabel">Please choose your meals per day</td>
                <td className = "scheduleGridLabel">Meals</td>
                <td className = "scheduleGridLabel">Snacks</td>
              </tr>
            </table>
            <div id = "scheduleGrid">
              <DaySelectorBlock day = "Sunday" increase = {(e) => this.increase(e)} decrease = {(e) => this.decrease(e)}/>
              <DaySelectorBlock day = "Monday" increase = {(e) => this.increase(e)} decrease = {(e) => this.decrease(e)}/>
              <DaySelectorBlock day = "Tuesday" increase = {(e) => this.increase(e)} decrease = {(e) => this.decrease(e)}/>
              <DaySelectorBlock day = "Wednesday" increase = {(e) => this.increase(e)} decrease = {(e) => this.decrease(e)}/>
              <DaySelectorBlock day = "Thursday" increase = {(e) => this.increase(e)} decrease = {(e) => this.decrease(e)}/>
              <DaySelectorBlock day = "Friday" increase = {(e) => this.increase(e)} decrease = {(e) => this.decrease(e)}/>
              <DaySelectorBlock day = "Saturday" increase = {(e) => this.increase(e)} decrease = {(e) => this.decrease(e)}/>
            </div>
            <button onClick = {() => this.finish()}>Save</button>
        </div>
    );
    }


  }

export default ScheduleForm;
