import React from 'react';
import axios from 'axios';
import './App.css';

const API_ENDPOINT= "http://127.0.0.0:8000"
const API_CLIENT = axios.create({
  baseURL: API_ENDPOINT,
  timeout: 10000
})
class  App extends React.Component {
  _onDragOver(e){
    e.preventDefault()
  }
  _onDragLeave(e){
    e.preventDefault()
  }
  _onDrop(e){
    e.preventDefault()
    var targetFile = e.dataTransfer.files[0]
    var data= new FormData()
    data.append('sound',targetFile)
    API_CLIENT.post('/classify', data, { headers: { "Content-Type": targetFile.type}})
      .then((response)=> {console.log(response)})
      .catch((error)=> {console.log(error)})
  }
  render(){
  return (
    <div className="App">
      <div 
        className ='file-dropzone'
        onDragOver={(e) => { this._onDragOver(e)}}
        onDragOver={(e) => { this._onDragOver(e)}}
        onDragOver={(e) => { this._onDragOver(e)}}>
    </div>
    </div>
  )
}
}

export default App;
