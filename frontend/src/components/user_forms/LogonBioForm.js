public class LogonBioForm extends Component{
  constructor(props){
    this.state = {

    }
  }

  render(){
    return (
      <div>
        <div id = "firstName">
            //style: text box
        </div>
        <div id = "lastName">
            //style: text box
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

export default NonLogonBioForm;
