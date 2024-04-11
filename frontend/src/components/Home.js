import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = ({settext, flag, setFlag}) => {
  const [files, setFiles] = useState([]);
  const backend=process.env.REACT_APP_BACKEND;
  let flag2;
  const nav=useNavigate();
  let mongoid;
  // useEffect(() => {
    const repeat=()=>{
      console.log("inside0");
      console.log(flag2);
      if(flag2)
      {
        console.log("inside1");
        setTimeout(async ()=>{
          console.log("inside2");
          let bodyContent = new FormData();
          bodyContent.append("flag", false);
          bodyContent.append("mongoid",mongoid);
          let response = await fetch(backend, { 
            method: "POST",
            body: bodyContent,
          });
          let data = await response.text();
          data=JSON.parse(data);
          let status=data["status"];
          let subsummary=data["summary"];
          settext(subsummary);
          setFlag(status);
          flag2=status;
          console.log(subsummary);
          console.log(status);
          console.log("inside3");
          repeat();
        },25000)
      }
    }
    // repeat();
  // }, [flag]); 
  const handleButtonClick = () => {
    const newFile = document.createElement("input");
    newFile.type = "file";
    newFile.id = `file-${files.length + 1}`;
    newFile.accept="application/pdf";
    newFile.addEventListener('change', (event) => {
      const selectedFile = event.target.files[0];
      console.log(selectedFile);
      if(selectedFile.type!=="application/pdf")
      {
        alert("Invalid document. Please upload PDF file");
        return;
      }
      // Use the functional form of setFiles to ensure you are updating based on the previous state
      setFiles(prevFiles => [...prevFiles, selectedFile]);
    });

    newFile.click();
  };
  const submitFiles= async(event)=>{
    event.preventDefault();
    // nav("/loading");
    console.log("called");
    console.log(typeof settext);
    console.log(settext);
    // let headersList = {
    //   "Access-Control-Allow-Headers": "Content-Type",
    //   "Access-Control-Allow-Origin": "*",
    //  }
     let bodyContent = new FormData();
     bodyContent.append("flag", true);
     for(let i of files)
     {
      bodyContent.append("file" ,i);
     }
     console.log("befor");
     try {
      nav("/summary");
      console.log(flag);
      setFlag(true);
      flag2=true;
      // setFlag(prevFlag => true);
      console.log(flag);
      let response = await fetch(backend, { 
        method: "POST",
        body: bodyContent,
        // headers: headersList
      });
      console.log(flag);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
    
      let data = await response.text();
      data=JSON.parse(data);
      console.log(flag);
      mongoid=data["mongoid"];
      // console.log(mongoid);
      if(mongoid==="SimErr")
      {
        nav("/");
        alert("Please give similar documents(of same domain)");
        return;
      }
      if(mongoid==="Error")
      {
        nav("/");
        alert(data["message"]);
        return;
      }
      console.log(flag);
      repeat();
      // setFlag(false);
      // settext(summary);
      // nav("/summary");

    } catch (error) {
      console.error('Fetch error:', error);
      if (error.response) {
        console.error('Response status:', error.response.status);
      }
    }
    
  }
  const deleteFile = (index) => {
    const updatedFiles = [...files];
    updatedFiles.splice(index, 1);
    setFiles(updatedFiles);
  };
  return (
    <div className='total'>
        <div className='center_div'>
          <h1 className='project_name'>Llama2 Multi-Document Summerization</h1>
          <div className='center_div_child'>
            <button className='add_file' onClick={handleButtonClick}>Add PDF Files</button>
            <div className='file_names_cover'>
              {files.map((file, index) => (
                <div className='file_names' key={index}><span onClick={() => deleteFile(index)}></span>{file.name}</div>
                
              ))}
            </div>
            <form onSubmit={submitFiles}>
            <input type='submit' className='btn btn-success'/>
            </form>
          </div>
        </div>
      
    </div>
  );
};

export default Home;
