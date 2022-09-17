import LogonBioForm from 'user_forms/LogonBioForm';
import NonLogonBioForm from 'user_forms/NonLogonBioForm';
import ScheduleInfo from 'user_forms/ScheduleInfo'
import Results from './Results'

class FormController extends Component {

  constructor(props){
    super(props);
    this.state = {
      logon: true,
      inError: false
    }
  }

  returnResults(props){
    return (
      <Results bio_info = "X" schedule_info = "y" />
    );
  }

  render(){
    if(this.state.logon == true){
      return (
        <div>
          <LogonBioForm bio_info = "x" />
          <ScheduleInfo schedule_info = "x" />
        {{if(this.state.inError = false){returnResults(this.state.bio_info, this.state.schedule_info);}}}
        </div>
      );
    } else {
      return (
        <NonLogonBioForm bio_info = "x" />
        <ScheduleInfo schedule_info = "x" />
        {
          if(this.state.inError = false){
              returnResults(bio_info, schedule_info);
          }
        }
      );
    }
  }
}

export default FormController;
