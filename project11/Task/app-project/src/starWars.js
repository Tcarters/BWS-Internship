import React, { useState } from 'react';
import './my.css';


const GetInfo = () => {  
    const [data, setData ] = useState(null);
    const [loading, setLoading] = useState(false);
    const [err, setError] = useState('');

   const handleSubmit = async () => { 

    const randomNumber = Math.round( Math.random() * 88 );
    // const url = `https://akabab.github.io/starwars-api/api/id/${randomNumber}.json`

    // const fetchData = async () => {
        try {
            const response = await fetch(`https://akabab.github.io/starwars-api/api/id/${randomNumber}.json`);
            // console.log('REsSPO:' , response );
            const jon = await response.json();
            // console.log('Got: ', jon );
            setData(jon);
            
        } catch (err) { 
            setError(err.message );
            console.log('Error retrieve api data:', err);
        } finally {
            setLoading(true);
            setError(false);
        }
};
    return( 
        <div> 
            { err && <h2> Searching ...</h2>}
               
                { !loading ?  <h2> Loading ...</h2>:
                    <>
                            
                <h1> Welcome To User Page </h1>    
                <img src= {data.image} className='my-img' alt='img' />

                <h3>Name: {data.name} </h3>
                <h4>Height: { data.height} cm </h4>
                <p>Gender: { data.gender} </p>
                <h3>HomeWorld: {data.homeworld} </h3>

                <ul> My Network Affiliation: </ul> 
                    <li>{ data.affiliations}</li>
            
                 </>
}
                <br /><br /><br />
                 <button 
                    type='submit'
                     onClick= { handleSubmit } 
                      className='btn'> Randomize Characters

                </button>


        </div>
    )
}

export default GetInfo;