import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {

  state = {title: '', content: '', image: null, existing_data: [{title: "hello"}, {title: "goodbye"}]};

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    })
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('image', this.state.image, this.state.image.name);
    form_data.append('title', this.state.title);
    form_data.append('content', this.state.content);
    let url = 'http://127.0.0.1:8000/api/posts/';
    axios.post(url, form_data, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
    .then(res => {console.log(res.data)})
    .catch(err => console.log(err))
  };

  componentDidMount() {
    axios.get(`http://127.0.0.1:8000/api/posts/`)
      .then(res => {
        const data = res.data;
        this.setState({ existing_data: data });
      })

    console.log("printing updated existing_data")
    console.log(this.state.existing_data)

  }

  getItems() {
    const items = this.state.existing_data.map( post => 
      <li> {post.title}  {post.image} </li> 
    );

    return (
      <ul> {items} </ul>
    );
  }

  render() {
    const list_items = this.getItems() 

    return (
      <div className="App">
        <div>
          <form onSubmit={this.handleSubmit}>
            <p>
              <input type="text" placeholder='Title' id='title' value={this.state.title} onChange={this.handleChange} required/>
            </p>
            <p>
              <input type="text" placeholder='Content' id='content' value={this.state.content} onChange={this.handleChange} required/>

            </p>
            <p>
              <input type="file"
                     id="image"
                     accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
            </p>
            <input type="submit"/>
          </form>
        </div>
          
        <div> 
          { list_items }
          <img alt="" src="/media/post_images/marissapang.jpg" width="200" height="600" />

        </div>
      </div>
    );
  }

}

export default App;

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
