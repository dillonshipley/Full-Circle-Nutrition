import {React, Component} from 'react';

class Tools extends Component {
    render(){
        return (
            <div>
                <button className = "backButton" onClick = {this.props.back}>Back</button>
            </div>
        );
    }
}

export default Tools;