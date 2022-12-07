import {React, Component} from 'react';

import AdminTools from './AdminTools';


class Tools extends Component {
    render(){
        return (
            <div>
                <button className = "backButton" onClick = {this.props.back}>Back</button>
                <AdminTools />
            </div>
        );
    }
}

export default Tools;
