const fat = 9;
const protein = 4;
const carb = 4;
const alc = 7;

const studyURL = "https://pubmed.ncbi.nlm.nih.gov/2305711/";

function LBTOKG(lb){
  return lb * .453592;
}

function MacroCalculator(props) {
      const weight = props[0];
      const height = props[1];
      const age = props[2];
      const sex = props[3];
      const activity = props[4];
      
      //weight in kg
      //height in cm
      var REE = (10 * weight) + (6.25 * height) + (5 * age);
      console.log(REE);
      if(sex === "M")
        REE = REE + 5;
      else
        REE = REE - 161;

      console.log("Resting Energy Expenditure: " + REE);



      return "x";
}

export default MacroCalculator
