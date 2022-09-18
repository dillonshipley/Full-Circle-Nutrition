import React, { Component } from 'react';

class Results extends Component{
  constructor(props){
    super(props);
    this.state = {
      bio_info: this.props.bio_info,
      schedule_info: this.props.schedule_info
    }
  }

  render(){
    return (
      <div></div>
    );
  }
}

export default Results;
