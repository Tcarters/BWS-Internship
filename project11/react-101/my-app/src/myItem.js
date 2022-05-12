import React from "react";



class Item extends React.Component {

    constructor (props) {
        super(props)

        this.state= {
            clicks: 0,
            totalRemaining: 100
        }
    }
    clickMe() {
        this.setState({
            clicks: this.state.clicks + 1,
            totalRemaining: this.state.totalRemaining - 1
        })

        // console.log("I was clicked", this.props.name )
    };

    // const my = {
    //     color: 'green',
    // };

    render() {
        return (
            <>  
            
            <h2 onClick={ () => this.clickMe() }> Hello from  {this.props.name}. </h2>
            <span>{this.state.clicks} is the number of clicks .{ this.state.totalRemaining } </span>
            
            </>
          
        )
    }
}

export default Item;