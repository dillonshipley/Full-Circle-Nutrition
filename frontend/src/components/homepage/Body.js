import React, { Component } from 'react';

import FormController from '../FormController'
import Results from '../Results'

class Body extends Component{
    constructor(props){
      super(props);
      this.state = {
        display: "start"
      }
    }

    swapToForms(){
      this.setState({display: "forms"});
    }

    render(){
      if(this.state.display === "forms"){
        return (
          <div>
            <FormController linkToHome = {() => this.setState({display: "start"})} />
          </div>
        )
      } else if (this.state.display === "start"){
        return (
            <div id = "mainBodyDiv">
                <div id = "homePageTitle">Goal to Table Nutrition </div>
                <div id = "homePageCardContainer">
                    <div className = "card" id = "homePageCard1" onClick = {() => this.swapToForms()}>Build From the Ground Up</div>
                    <div className = "card" id = "homePageCard2">Use One of Our Tools</div>
                </div>
                <div className = "homepageLoginText">
                    Log in for the complete experience
                </div>
            </div>
        )
      } else if (this.state.display === "results"){
          <Results />
      }
    }
}

export default Body;
