const fatCals = 9;
//const proteinCals = 4;
const carbCals = 4;
//const alcCals = 7;

//const studyURL = "https://pubmed.ncbi.nlm.nih.gov/2305711/";

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

      //console.log(weightType);
      if(weightType === "LB")
        weight = LBTOKG(weight)
      if(heightType === "IN")
        height = INTOCM(height)

      let activityRatio = 0;
      switch(activity){
        case "Sedentary":
          activityRatio = 1.2;
          break;
        case "Lightly Active":
          activityRatio = 1.375;
          break;
        case "Moderately Active":
          activityRatio = 1.55;
          break;
        case "Active":
          activityRatio = 1.725;
          break;
        case "Very Active":
          activityRatio = 1.9;
          break;
        default:
          break;
      }

      //weight in kg
      //height in cm
      let REE = (10 * weight) + (6.25 * height) + (5 * age);
      REE = (sex === "M") ? (REE + 5) : (REE + 161);

      var TDEE = Math.round(REE * activityRatio);

      switch(goal){
        case "Rapid Loss":
          TDEE = TDEE - 600;
          break;
        case "Moderate Loss":
          TDEE = TDEE - 400;
          break;
        case "Slight Loss":
          TDEE = TDEE - 250;
          break;
        case "Neutral":
            break;
        case "Slight Gain":
          TDEE = TDEE + 250;
          break;
        case "Moderate Gain":
          TDEE = TDEE + 400;
          break;
        case "Rapid Gain":
          TDEE = TDEE + 600;
          break;
        default:
        break;
      }

       var protein = Math.round(KGTOLB(weight));
       var calsFromProtein = 4 * weight;

       //ratio of carbs : remaining calories after protein
       var carbRatio = .5;

       var calsFromCarbs = Math.round((TDEE - calsFromProtein) * carbRatio);
       var calsFromFats = TDEE - calsFromProtein - calsFromCarbs;

      var carbs = calsFromCarbs / carbCals;
      var fats = calsFromFats / fatCals;

      //console.log("protein: " + protein + " fats: " + fats + " carbs: " + carbs);

      return [protein, fats, carbs, TDEE];
}

export default MacroCalculator
