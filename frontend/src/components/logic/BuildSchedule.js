import React, {Component} from 'react';

export default class BuildSchedule extends Component{
  constructor(props){
    super(props);
    this.state = {
      meals: [];
      completed: false;
      mealsRemaining = props.meals;
    }
  }

  calculate(){
    proteinSupplements();
    findProteinMeals();

  }

}
