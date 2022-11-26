import React, { Component } from 'react';

import FormController from '../FormController';
import Results from '../Results';
import Login from '../Login';
import Tools from '../tools/Tools';
import Homepage from './Homepage.js';






//var cardTextOneTitle = "BUILD";
//var cardTextOneDetail = "from the ground up"

//var cardTextOneTitle = "EXPERIMENT";



class Body extends Component{
    constructor(props){
      super(props);
      this.state = JSON.parse(localStorage.getItem('navState')) || {
          display: "start"
      }
    }

    changeDisplay(display){
      console.log("display: " + display);
      this.setState({display: display}, () => {
        localStorage.setItem('navState', JSON.stringify(this.state));
      });
    }

    render(){
      if(this.state.display === "forms"){
        return (
          <div>
            <FormController back = {() => this.changeDisplay("start")} />
          </div>
        )
      } else if (this.state.display === "start"){
        return (
          <Homepage change = {(e) => this.changeDisplay(e)}/>
        );
      } else if (this.state.display === "results"){
          <Results />
      }else if (this.state.display === "login"){
        return(
          <Login back = {() =>this.changeDisplay("start")}/>
        );
      } else if (this.state.display === "tools"){
        return(
            <Tools back = {() =>this.changeDisplay("start")}/>
        );
      }
    }
}

export default Body;
