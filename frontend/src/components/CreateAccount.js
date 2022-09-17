public class CreateAccount extends Component{
  render(){
    return (
      <div>
        <div id = "registerUsername">
            //style: text box
        </div>
        <div id = "registerPassword">
            //style: text box
        </div>
        <div id = "firstName">
            //style: text box
        </div>
        <div id = "lastName">
            //style: text box
        </div>
        <div id = "email">
            //style: text box (optional)
        </div>
        <div id = "height">
            //style: slider
        </div>
        <div id = "currentWeight">
            //style: text box
        </div>
        <div id = "bodyFat">
            //style: dropdown (optional, rough estimate)
        </div>
      </div>
    );
  }
}

export default BioForm;
