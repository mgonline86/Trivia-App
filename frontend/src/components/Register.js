import React, { Component } from 'react';
import $ from 'jquery';
import logo from '../logo.svg';
import '../stylesheets/Login.css';

class Register extends Component {

  constructor(){
    super();
    this.state = {
      username: '',
      password: '',
      user_exist: false
    }
  }

  navTo(uri){

      window.location.href = window.location.origin + uri;

    
  }


  registerUser = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/register', 
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        username: this.state.username,
        password: this.state.password
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        this.setState({
          user_exist: result.user_exist
        })
        let user_exist=result.user_exist
        console.log(user_exist);
        return user_exist;
      },
      error: (error) => {
        alert('Unable to Login')
        return;
      }
    })
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
  }

  render() {
    return (
      <div className="App-login">
        <form className="form-view" id="user-login" onSubmit={this.registerUser}>
          <div id="welcome">Register</div>
          <label>
            Username:
            <input type="text" name="username" onChange={this.handleChange} required/>
          </label>
          <label>
            Password:
            <input type="text" name="password" onChange={this.handleChange} required/>
          </label>
          <input type="submit" className="button" value="Register" onClick={() => {this.navTo('/')}}/>
          <div class="anchor"><a href="/">User Login</a></div>
        </form>
      </div>
    );
  }
}

export default Register;
