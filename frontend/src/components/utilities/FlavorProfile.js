import React, {useState} from 'react';
import '../user_forms/PreferencesForm.css';

export default function FlavorProfile(props){

  const [isExpanded, setIsExpanded] = useState(false);

  function setIsExpandedWrapper(){
    document.getElementById("FP" + props.num).classList.add("selected");
  }

  return (
    <div id = {"FP" + props.num} className = "flavorProfileOutline" onClick = {() => setIsExpandedWrapper()}>
      {props.type}
    </div>
  );
}
