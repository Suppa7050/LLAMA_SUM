import logo from './logo.svg';
import {Route, Routes, BrowserRouter as Router} from "react-router-dom";
import './App.css';
import Home from './components/Home';
import Summary from './components/Summary';
import { useState } from 'react';
import Loading from './Loading';

function App() {
  const [text, settext]=useState("");
  // const [flag,setFlag]=useState(false);
  let [flag,setFlag]=useState(false);
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home settext={settext} flag={flag} setFlag={setFlag}/>}/>
        <Route path='/summary' element={<Summary text={text} flag={flag}/>} />
        <Route path='/loading' element={<Loading/>} />
      </Routes>
    </Router>
  );
}

export default App;
