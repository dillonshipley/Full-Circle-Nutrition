import React, {Component} from 'react';

export default class Day extends Component{
  constructor(props){
    super(props);
    this.state = {
      carbs: props.carbs,
      cals: props.cals,
      fat: props.fat,
      protein: props.protein,
      meals: props.meals,
      snacks: props.snacks
    }
  }

  add(meal, isMeal){
    this.state.carbs = this.state.carbs - meal.carbs;
    this.state.cals = this.state.cals - meal.cals;
    this.state.fat = this.state.carbs - meal.fat;
    this.state.protein = this.state.protein - meal.protein;
    if(isMeal)
      this.state.meals = this.state.meals - 1;
    else
      this.state.snacks = this.state.snacks - 1;
  }
}
