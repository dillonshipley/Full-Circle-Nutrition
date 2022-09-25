import React, { Component } from 'react';

const fat = 9;
const protein = 4;
const carb = 4;
const alc = 7;

const studyURL = "https://pubmed.ncbi.nlm.nih.gov/2305711/";

function MacroCalculator(props) {
      const weight = props[1];
      const height = props[2];
      const age = props[3];
      const sex = props[4];
      const activity = props[5];

      var REE = 10 * weight;
      REE = REE + (6.25 * height);
      REE = REE - 5 * age;

      if(sex === "M")
        REE = REE + 5;
      else
        REE = REE - 161;

      console.log("Resting Energy Expenditure: " + REE);



      return "x";
}

export default MacroCalculator
