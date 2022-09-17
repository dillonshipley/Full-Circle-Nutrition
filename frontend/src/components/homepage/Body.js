import FormController from '../FormController'

class Body extends Component{
    constructor(props){
      super(props);
      this.state = {
        display: "start"
      }
    }

    swapToForms(){
      this.setState({display: forms});
    }

    render(){
      if(this.state.display == "forms"){

      } else if (this.state.display == "start"){
        return (
            <div id = "mainBodyDiv">
                <div id = "homePageTitle">Goal to Table Nutrition </div>
                <div id = "homePageCardContainer">
                    <div className = "card" id = "homePageCard1" onClick = {swapToForms()}>Build From the Ground Up</div>
                    <div className = "card" id = "homePageCard2">Use One of Our Tools</div>
                </div>
                <div class = "homepageLoginText">
                    Log in for the complete experience
                </div>
            </div>
        )
      }
    }
}

export default Body;
