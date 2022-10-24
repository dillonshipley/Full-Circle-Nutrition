
const fatCals = 9;
const proteinCals = 4;
const carbCals = 4;
const alcCals = 7;

const studyURL = "https://pubmed.ncbi.nlm.nih.gov/2305711/";

function LBTOKG(lb){
  return lb * .453592;
}

function KGTOLB(kg){
  return kg / .453592;
}

function INTOCM(inches){
  return inches * 2.54;
}

function MacroCalculator(valueData, typeData) {
      let weight = valueData[0];
      const weightType = typeData[0];
      let height = valueData[1];
      const heightType = typeData[1];
      const age = valueData[2];
      const sex = valueData[3];
      const activity = valueData[4];
      const goal = valueData[5];

      console.log(weightType);
      if(weightType == "LB")
        weight = LBTOKG(weight)
      if(heightType === "IN")
        height = INTOCM(height)

      //weight in kg
      //height in cm
      var REE = (10 * weight) + (6.25 * height) + (5 * age);
      console.log(REE);
      if(sex === "M")
        REE = REE + 5;
      else
        REE = REE - 161;

       var TDEE = Math.round(REE * activity);
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

       var protein = Math.round(KGTOLB(weight));
       var calsFromProtein = 4 * weight;

       //ratio of carbs : remaining calories after protein
       var carbRatio = .5;

       var calsFromCarbs = Math.round((TDEE - calsFromProtein) * carbRatio);
       var calsFromFats = TDEE - calsFromProtein - calsFromCarbs;

      var carbs = calsFromCarbs / carbCals;
      var fats = calsFromFats / fatCals;

      console.log("protein: " + protein + " fats: " + fats + " carbs: " + carbs);

      return [protein, fats, carbs, TDEE];
}

export default MacroCalculator
