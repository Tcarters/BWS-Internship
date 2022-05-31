// import logo from './logo.svg';
import './App.css';
import './myItem';
// import Item from './myItem';
import React from 'react';


// const mycss = {
//   margin: '40px',
//   background-color: yellow
// };
class FilmItemRow extends React.Component {
  render() {
    return (
      <li> <a href={this.props.url}> {this.props.url} </a>
      </li>
    )
  }
}

class StarWars extends React.Component {
  constructor() {
    super()

    this.state = {
      loadedCharacter: false,
      name: null,
      height: null,
      homeworld: null,
      films: [],
    }
  }
  getNewCharacter() {
    // console.log("Get new Character from a button ");
    const randomNumber = Math.round( Math.random() * 82 )
    const url = `https://swapi.dev/api/people/${randomNumber}/`
    fetch(url)
        .then(response => response.json() )
        .then( data => {
            //console.log(data) 
              this.setState({
              name: data.name,
              height: data.height,
              homeworld: data.homeworld,
              films:  data.films,
              loadedCharacter: true
    })
        })
  }
  render() {

    const movies = this.state.films.map((url, i) => {
        return <FilmItemRow  key={i} url={url} />
  })


    return(
      <div>
         {
           this.state.loadedCharacter &&
           <div>
              <h1>Name: {this.state.name} </h1>
              <p>{this.state.height} cm </p>
              <p><a href={this.state.homeworld}>Homeworld</a> </p>
              <ul>
                { movies }
              </ul>
             </div>
  }
              <button 
              type='button' 
              onClick={ () => this.getNewCharacter() } 
              className='btn'> Randomize Character
            </button>

      </div>
    )

  }
}

function App() {

  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

        <Item  name= {"Gully jon "}  className="mycss"  />
        <Item name={"Kallob Tory"} />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}

      <header className='App-header'>
          <StarWars />
      </header> 
    </div>
  );
}

export default App;
