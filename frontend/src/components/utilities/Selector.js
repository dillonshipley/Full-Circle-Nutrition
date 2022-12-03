import React, { useState, useEffect } from 'react';

function Selector(props){
  const [optionSelected, setOptionSelected] = useState(props.options[0]);

  useEffect(() => {
    document.getElementById(optionSelected + "Option").classList.add("selected");
  });

  function setSelectedWrapper(value){
    if(optionSelected ===  value)
      return; //no additional logic, not switching

    document.getElementById(optionSelected + "Option").classList.remove("selected");
    document.getElementById(value + "Option").classList.add("selected");
    setOptionSelected(value);
    props.setType(value);
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
