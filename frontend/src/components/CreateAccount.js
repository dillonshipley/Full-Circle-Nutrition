public class CreateAccount extends Component{
  render(){
    return (
      <div>
        <div id = "registerAccountHeader">Register New Account</div>
        <div className = "registerAccountSectionHeader">
        <div id = "registerUsername">
            <input placeholder = "USERNAME" type = "text" id = "usernameInput" name = "username" className = "textInput"/>
        </div>
        <div id = "registerPassword">
            <p>Password:</p>
            <input type = "text" id = "passwordInput" name = "password" className = "textInput"/>
        </div>
        <div id = "confirmPassword">
            <p>Confirm your password:</p>
            <input type = "text" id = "passwordConfirmInput" name = "passwordConfirm" className = "textInput"/>
        </div>
        <div id = "firstName">
            <p>First Name:</p>
            <input type = "text" id = "firstNameInput" name = "firstName" className = "textInput"/>
        </div>
        <div id = "lastName">
            <p>Last Name:</p>
            <input type = "text" id = "lastNameInput"
        </div>
        <div id = "email">
            <p>Email Address:</p>
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
