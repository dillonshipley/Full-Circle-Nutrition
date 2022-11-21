class CreateAccount extends Component{

  save(){
    var data = [
      document.getElementById("usernameInput").value,
      document.getElementById("passWordInput").value,
      document.getElementById("emailInput").value,
      document.getElementById("heightInput").value,
      document.getElementById("weightInput").value,
      document.getElementById("bodyfatInput").value,
      document.getElementById("bodyfatInput").value
    ]

    //async function createUser(this.state.data){
    //  var query =
    //  `?data`
    //}
  }

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
            <input placeholder = "PASSWORD" type = "text" id = "passwordInput" name = "password" className = "textInput"/>
        </div>
        <div id = "confirmPassword">
            <p>Confirm your password:</p>
            <input type = "text" id = "passwordConfirmInput" name = "passwordConfirm" className = "textInput"/>
        </div>
        <div id = "email">
            <p>Email Address:</p>
            <input type = "text" id = "emailInput" name = "email" className = "textInput"/>
        </div>
        <div id = "height">
            <p>Height:</p>
            <input type = "text" id = "heightInput" name = "height" className = "textInput"/>
        </div>
        </div>
        <div id = "currentWeight">
          <p>Height:</p>
          <input type = "text" id = "weightInput" name = "currentWeight" className = "textInput"/>
        </div>
        <div id = "bodyFat">
        <p>Height:</p>
        <input type = "combobox" id = "bodyfatInput" name = "bodyFat" className = "textInput"/>
        </div>
        <div id = "goalVector">
          <p>Goal Direction:</p>
          <input type = "text" id = "goalInput" name = "goal" className = "textInput"/>
      </div>
        <div></div>
      </div>
    );
  }
}

export default BioForm;
