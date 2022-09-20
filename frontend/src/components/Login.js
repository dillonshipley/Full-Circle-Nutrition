import React, { Component } from 'react';

class Login extends Component{
  constructor(props){
    super(props);
    this.state = {
      data: props.data
    }
  }

  componentDidMount(){
    console.log("AAA");
  }

  render(){
    return (
      <div>
          <button className = "backButton" onClick = {this.props.back}>Back</button>
          <div id = "loginUsername"></div>
          <div id = "loginPassword"></div>
      </div>
    );
  }
}

export default Login;
