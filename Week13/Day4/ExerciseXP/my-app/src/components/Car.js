import {Component, React} from 'react';

class Car extends Component{
    constructor(props){
        super(props);
        this.state= {
            color:'Red'
        }
        
    }
    render(){
        console.log(this.props);
        return(
        <>
        <header>This car is a {`${this.state.color} ${this.props.data.model}`}</header>
        </>
        )
    }
        
    
}

export default Car;