public class NonLogonBioForm extends Component{
  constructor(props){
    this.state = {
      data: props.data;
    }
  }

  render(){
    return (
      <div>
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
