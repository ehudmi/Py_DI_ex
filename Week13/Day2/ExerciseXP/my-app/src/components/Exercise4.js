import logo from 'C:/Github/Py_DI_ex/Week13/Day2/ExerciseXP/my-app/src/logo.svg';
import './Exercise4.css';
const Exercise4 =(props)=>{
    const style_header={
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    }
    return(
        <>
        <h1 style={style_header}>This is a Header</h1>
        <p className='para'>This is a paragraph</p>
        <a href="#">This is a link</a>
        <form>
            <h2>This is a form</h2>
            <h4>Enter your name</h4>
            <input type="text"></input><button type="submit">Submit</button>
            </form>
            <h4 style={{fontWeight:"bold"}}>Here is an image</h4>
            <img alt="logo" src={logo}/>
            <h4>This is a list</h4>
            <ul>
                <li>Coffee</li>
                <li>Tea</li>
                <li>Milk</li>
            </ul>
        
        </>
    )
}

export default Exercise4;