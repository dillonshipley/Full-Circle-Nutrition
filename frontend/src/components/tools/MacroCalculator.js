const fatCals = 9;
const proteinCals = 4;
const carbCals = 4;
const alcCals = 7;

const studyURL = "https://pubmed.ncbi.nlm.nih.gov/2305711/";

function LBTOKG(lb){
  return lb * .453592;
}

function MacroCalculator(props) {
      const weight = props[0];
      const weightType = props[1];
      const height = props[2];
      const age = props[3];
      const sex = props[4];
      const activity = props[5];
      const goal = props[6];

      console.log("GOT " + weightType);

      //weight in kg
      //height in cm
      var REE = (10 * weight) + (6.25 * height) + (5 * age);
      console.log(REE);
      if(sex === "M")
        REE = REE + 5;
      else
        REE = REE - 161;

      console.log("Resting Energy Expenditure: " + REE);

      console.log("activity: " + activity);
       var TDEE = REE * activity;

       console.log("TDEE: " + TDEE);

      switch(goal){
        case "rloss":
          TDEE = TDEE - 600;
          break;
        case "mloss":
          TDEE = TDEE - 400;
          break;
        case "sloss":
          TDEE = TDEE - 250;
          break;
        case "netural":
            break;
        case "sgain":
          TDEE = TDEE + 250;
          break;
        case "mgain":
          TDEE = TDEE + 400;
          break;
        case "rgain":
          TDEE = TDEE + 600;
          break;
      }

      console.log("new TDEE: " + TDEE);

       var protein = weight;
       var calsFromProtein = 4 * weight;

       var carbRatio = 45;
       var fatRatio = 25;

       var calsFromCarbs = (TDEE - calsFromProtein) / 100 * carbRatio;
       var calsFromFats = TDEE - calsFromProtein - calsFromCarbs;

      var carbs = calsFromCarbs / carbCals;
      var fats = calsFromFats / fatCals;

      console.log("protein: " + protein + " fats: " + fats + " carbs: " + carbs);

      return "x";
}

export default MacroCalculator
