public class LogonBioForm extends Component{
  constructor(props){
    super(props);
    this.state = {
      data: props.data;
    }
  }


  render(){
    return (
      <div>
          <div id = "loginUsername"></div>
          <div id = "loginPassword"></div>
      </div>
    );
  }
}

export default LogonBioForm;
