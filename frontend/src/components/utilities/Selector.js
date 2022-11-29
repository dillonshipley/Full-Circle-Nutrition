import React, { useState } from 'react';

function Selector(props){
  const [optionSelected, setOptionSelected] = useState("");

  function setSelectedWrapper(value){
    if(optionSelected === value + "Option")
      return; //no additional logic, not switching
    else if(optionSelected !== "")
      document.getElementById(optionSelected).classList.remove("selected");

    document.getElementById(value + "Option").classList.add("selected");
    setOptionSelected(value + "Option");
    props.setType({type: props.type + "Type", option: value})
  }

  return (
    <div className = "selectorContainer">
      <div className = "selectorGrid">
          {props.options?.map(option => (
            <div id = {option + "Option"} className = "selectorOption" key = {option} onClick = {(e) => setSelectedWrapper(option)}>{option}</div>
          ))}
      </div>
    </div>
  );
}

export default Selector;
